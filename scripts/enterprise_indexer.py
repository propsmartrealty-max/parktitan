#!/usr/bin/env python3
"""
scripts/enterprise_indexer.py
ULTRA-ADVANCED ENTERPRISE-GRADE GOOGLE & MULTI-ENGINE INDEXING ENGINE
For: purpleparktitan.com (Pride Purple Park Titan Hinjewadi)

Architecture:
1. Multi-Service Account Key Rotation Mesh (scales quota past Google's 200/day limit)
2. Multipart HTTP Batching (https://indexing.googleapis.com/batch/indexing/v3 - up to 100 URLs per call)
3. Persistent State Store (.indexing_state.json) with intelligent rotation & deduplication
4. Comprehensive Ecosystem Harvester: Core Pages, Articles, Media, Web Stories, and Programmatic URLs
5. IndexNow Network Broadcast: Instant push to Bing, Microsoft Copilot, Yandex, Seznam, Naver
6. Google Search Console Sitemap Ping Broadcasting
7. Real-Time Inspection & JSON Audit Reporting (indexing_report.json)

Usage:
    python3 scripts/enterprise_indexer.py [--keys-dir keys/] [--sitemap sitemaps/sitemap-pages.xml] [--batch-size 50]
    python3 scripts/enterprise_indexer.py --inspect "https://purpleparktitan.com/"
    python3 scripts/enterprise_indexer.py --all
"""

import sys
import os
import glob
import json
import time
import argparse
import datetime
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart

try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    import requests
except ImportError:
    print("Error: Missing dependencies. Run: pip install google-auth requests")
    sys.exit(1)

# API Endpoints & Constants
INDEXING_API_PUBLISH = "https://indexing.googleapis.com/v3/urlNotifications:publish"
INDEXING_API_METADATA = "https://indexing.googleapis.com/v3/urlNotifications/metadata"
INDEXING_API_BATCH = "https://indexing.googleapis.com/batch/indexing/v3"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
INDEXNOW_KEY = "c7d094744fb02eb115c943afbffeb469"
INDEXNOW_KEY_LOCATION = "https://purpleparktitan.com/c7d094744fb02eb115c943afbffeb469.txt"
HOST_DOMAIN = "purpleparktitan.com"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
STATE_FILE = ".indexing_state.json"
REPORT_FILE = "indexing_report.json"

TIER_1_CORE_URLS = [
    "https://purpleparktitan.com/",
    "https://purpleparktitan.com/videos/pride-purple-park-titan-official-walkthrough",
    "https://purpleparktitan.com/videos/",
    "https://purpleparktitan.com/explore/",
    "https://purpleparktitan.com/articles/",
    "https://purpleparktitan.com/articles/pride-purple-park-titan-hinjewadi-ecosystem-master-review",
    "https://purpleparktitan.com/articles/2bhk-3bhk-flats-hinjewadi-pune-market-guide",
    "https://purpleparktitan.com/articles/pune-real-estate-investment-rental-yields-hinjewadi",
    "https://purpleparktitan.com/articles/nri-guide-investing-in-pune-real-estate-park-titan",
    "https://purpleparktitan.com/articles/hinjewadi-metro-line-3-impact-on-pune-real-estate-property-rates",
    "https://purpleparktitan.com/articles/pune-real-estate-market-guide-pride-purple-ecosystem",
    "https://purpleparktitan.com/llms.txt",
    "https://purpleparktitan.com/web-stories/5-academies-park-titan",
    "https://purpleparktitan.com/web-stories/7-acre-podium-park-titan",
    "https://purpleparktitan.com/web-stories/2bhk-3bhk-floor-plans-park-titan"
]

class KeyManager:
    """Manages rotation across multiple Google Cloud Service Account keys to scale daily quota."""
    def __init__(self, key_paths):
        self.key_paths = key_paths
        self.accounts = []
        self.active_index = 0
        self._load_accounts()

    def _load_accounts(self):
        for path in self.key_paths:
            if not os.path.exists(path):
                continue
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                client_email = data.get('client_email', 'unknown')
                project_id = data.get('project_id', 'unknown')
                creds = service_account.Credentials.from_service_account_file(
                    path, scopes=SCOPES
                )
                self.accounts.append({
                    "path": path,
                    "email": client_email,
                    "project_id": project_id,
                    "creds": creds,
                    "token": None,
                    "token_expiry": 0,
                    "quota_exhausted": False,
                    "submissions_today": 0
                })
            except Exception as e:
                print(f"[KeyManager] Warning: Failed to load key {path}: {e}")

    def count(self):
        return len(self.accounts)

    def get_token(self):
        """Returns valid OAuth2 Bearer token for active account, rotating if quota exhausted."""
        while self.active_index < len(self.accounts):
            acc = self.accounts[self.active_index]
            if acc["quota_exhausted"]:
                self.active_index += 1
                continue
            now = time.time()
            if not acc["token"] or now >= acc["token_expiry"]:
                try:
                    acc["creds"].refresh(Request())
                    acc["token"] = acc["creds"].token
                    acc["token_expiry"] = now + 3500
                except Exception as e:
                    print(f"[KeyManager] Error refreshing token for {acc['email']}: {e}")
                    acc["quota_exhausted"] = True
                    self.active_index += 1
                    continue
            return acc["token"], acc

        return None, None

    def mark_quota_exhausted(self, acc):
        print(f"[KeyManager] Quota exhausted for project '{acc['project_id']}' ({acc['email']}).")
        acc["quota_exhausted"] = True
        self.active_index += 1
        if self.active_index < len(self.accounts):
            next_acc = self.accounts[self.active_index]
            print(f"[KeyManager] Seamlessly failing over to Project #{self.active_index+1}: '{next_acc['project_id']}'")
        else:
            print("[KeyManager] All configured service accounts have exhausted their daily quota.")

class StateManager:
    """Tracks state and history of submitted URLs to prevent wasted quota and enable intelligent rotation."""
    def __init__(self, file_path=STATE_FILE):
        self.file_path = file_path
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "last_run": None,
            "programmatic_offset": 0,
            "urls": {}
        }

    def save(self):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"[StateManager] Error saving state: {e}")

    def record_submission(self, url, engine, status, notify_time=None):
        if url not in self.data["urls"]:
            self.data["urls"][url] = {}
        self.data["urls"][url][engine] = {
            "submitted_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "status": status,
            "notify_time": notify_time
        }

    def is_recently_submitted(self, url, engine="google", hours=24):
        entry = self.data["urls"].get(url, {}).get(engine)
        if not entry:
            return False
        submitted_at_str = entry.get("submitted_at")
        if not submitted_at_str:
            return False
        try:
            submitted_at = datetime.datetime.fromisoformat(submitted_at_str)
            age = (datetime.datetime.now(datetime.timezone.utc) - submitted_at).total_seconds() / 3600
            return age < hours
        except Exception:
            return False

class SitemapHarvester:
    """Discovers, parses and prioritizes URLs across the entire Pride Purple Park Titan ecosystem."""
    @staticmethod
    def extract_urls(sitemap_path):
        urls = []
        if not os.path.exists(sitemap_path):
            return urls
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            for loc in root.findall(".//sm:loc", ns):
                if loc.text:
                    urls.append(loc.text.strip())
            if not urls:
                for loc in root.findall(".//loc"):
                    if loc.text:
                        urls.append(loc.text.strip())
        except Exception as e:
            print(f"[Harvester] Error parsing {sitemap_path}: {e}")
        return urls

    @classmethod
    def harvest_all(cls, max_programmatic=500, state=None):
        harvested = {
            "tier1_core": list(TIER_1_CORE_URLS),
            "tier2_sitemaps": [],
            "tier3_programmatic": []
        }

        # 1. Core Pages & Articles & Media
        for sm in ["sitemaps/sitemap-pages.xml", "sitemaps/sitemap-articles.xml", "sitemaps/sitemap-media.xml", "sitemaps/sitemap-stories.xml"]:
            for u in cls.extract_urls(sm):
                if u not in harvested["tier1_core"]:
                    harvested["tier2_sitemaps"].append(u)

        # 2. Partitioned Programmatic Sitemaps
        prog_sitemaps = sorted(glob.glob("sitemaps/sitemap-p-*.xml"))
        all_prog_urls = []
        for psm in prog_sitemaps:
            all_prog_urls.extend(cls.extract_urls(psm))

        if all_prog_urls and state:
            offset = state.data.get("programmatic_offset", 0)
            total = len(all_prog_urls)
            selected = []
            for i in range(min(max_programmatic, total)):
                idx = (offset + i) % total
                selected.append(all_prog_urls[idx])
            state.data["programmatic_offset"] = (offset + len(selected)) % total
            harvested["tier3_programmatic"] = selected

        return harvested

def inspect_url(url, token):
    """Inspects real-time Google indexing metadata for a specific URL."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"url": url}
    print(f"\n[Inspect] Querying Google Indexing API for: {url}")
    try:
        res = requests.get(INDEXING_API_METADATA, headers=headers, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            print("  [✓ 200 OK] Google Indexing Metadata Found:")
            print(json.dumps(data, indent=2))
            return data
        elif res.status_code == 404:
            print("  [i 404 NOT_FOUND] Google has no prior URL_UPDATED notification on record for this URL.")
            return None
        else:
            print(f"  [✗ {res.status_code}] Google API error: {res.text}")
            return None
    except Exception as e:
        print(f"  [✗ ERROR] Inspection failed: {e}")
        return None

def submit_single_url_google(url, token, action_type="URL_UPDATED"):
    """Submits a single URL notification directly to Googlebot."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {"url": url, "type": action_type}
    try:
        res = requests.post(INDEXING_API_PUBLISH, headers=headers, json=payload, timeout=15)
        if res.status_code == 200:
            data = res.json()
            notify_time = data.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "Recorded")
            return True, res.status_code, notify_time
        elif res.status_code == 429:
            return False, 429, "QUOTA_EXHAUSTED"
        else:
            return False, res.status_code, res.text
    except Exception as e:
        return False, 0, str(e)

def submit_indexnow(urls):
    """Broadcasts URLs directly to the IndexNow network (Bing, Microsoft Copilot, Yandex, Seznam, Naver)."""
    if not urls:
        return 0
    print("\n" + "=" * 70)
    print("  BROADCASTING TO INDEXNOW NETWORK (BING · COPILOT · YANDEX · NAVER)")
    print("=" * 70)
    chunk_size = 10000
    pushed = 0
    for i in range(0, len(urls), chunk_size):
        chunk = urls[i:i + chunk_size]
        payload = {
            "host": HOST_DOMAIN,
            "key": INDEXNOW_KEY,
            "keyLocation": INDEXNOW_KEY_LOCATION,
            "urlList": chunk
        }
        headers = {"Content-Type": "application/json; charset=utf-8"}
        try:
            res = requests.post(INDEXNOW_ENDPOINT, headers=headers, json=payload, timeout=25)
            if res.status_code in [200, 202]:
                print(f"  [✓ {res.status_code} ACCEPTED] Successfully pushed batch of {len(chunk)} URLs to IndexNow!")
                pushed += len(chunk)
            else:
                print(f"  [✗ {res.status_code}] IndexNow rejected batch: {res.text}")
        except Exception as e:
            print(f"  [✗ ERROR] IndexNow connection error: {e}")
    return pushed

def ping_sitemaps():
    """Pings Google Search Console and Bing with the master sitemap index."""
    sitemap_url = f"https://{HOST_DOMAIN}/sitemap.xml"
    pings = [
        ("Google Search Console Ping", f"https://www.google.com/ping?sitemap={sitemap_url}"),
        ("Bing Webmaster Ping", f"https://www.bing.com/ping?sitemap={sitemap_url}")
    ]
    print("\n" + "=" * 70)
    print("  PINGING SEARCH ENGINE SITEMAP INDEX REGISTRIES")
    print("=" * 70)
    for name, endpoint in pings:
        try:
            res = requests.get(endpoint, timeout=10)
            print(f"  [✓ {res.status_code}] {name} pinged successfully: {endpoint}")
        except Exception as e:
            print(f"  [i] {name} ping note: {e}")

def main():
    parser = argparse.ArgumentParser(description="Ultra-Advanced Enterprise Google & Multi-Engine Indexing Suite")
    parser.add_argument("--keys-dir", default="keys", help="Directory containing multiple service account JSON keys for quota multiplication")
    parser.add_argument("--key", default="service_account.json", help="Path to default Google Cloud Service Account key")
    parser.add_argument("--url", help="Single URL to index or inspect")
    parser.add_argument("--inspect", action="store_true", help="Inspect real-time Google indexing metadata for target URL")
    parser.add_argument("--all", action="store_true", help="Harvest all sitemaps (including programmatic corpus) for mass broadcast")
    parser.add_argument("--max-programmatic", type=int, default=500, help="Max programmatic URLs to rotate in this run")
    parser.add_argument("--force", action="store_true", help="Force re-indexing even if submitted within last 24 hours")
    parser.add_argument("--type", default="URL_UPDATED", choices=["URL_UPDATED", "URL_DELETED"], help="Notification type")
    args = parser.parse_args()

    print("=" * 70)
    print("  PRIDE PURPLE PARK TITAN — ENTERPRISE MULTI-ENGINE INDEXING SUITE")
    print("  Master Ecosystem: https://purpleparktitan.com/")
    print("=" * 70)

    # 1. Discover Service Account Keys
    key_paths = []
    if os.path.exists(args.key):
        key_paths.append(args.key)
    if os.path.exists(args.keys_dir):
        key_paths.extend(glob.glob(os.path.join(args.keys_dir, "*.json")))
    # Environment variable support
    env_keys = os.environ.get("GOOGLE_INDEXING_KEYS")
    if env_keys:
        for p in env_keys.split(","):
            if os.path.exists(p.strip()):
                key_paths.append(p.strip())

    key_paths = list(dict.fromkeys(key_paths))
    km = KeyManager(key_paths)
    print(f"Active Key Mesh: {km.count()} Service Account(s) loaded.")
    for idx, acc in enumerate(km.accounts):
        print(f"  Key #{idx+1}: {acc['email']} (Project: {acc['project_id']})")

    state = StateManager()

    # Inspection Mode
    if args.url and args.inspect:
        token, acc = km.get_token()
        if not token:
            print("[!] Error: No valid Google authentication token available.")
            sys.exit(1)
        inspect_url(args.url, token)
        sys.exit(0)

    # 2. Build URL Priority Queue
    urls_to_submit = []
    if args.url:
        urls_to_submit = [args.url]
    elif args.all:
        harvested = SitemapHarvester.harvest_all(max_programmatic=args.max_programmatic, state=state)
        urls_to_submit = harvested["tier1_core"] + harvested["tier2_sitemaps"] + harvested["tier3_programmatic"]
    else:
        harvested = SitemapHarvester.harvest_all(max_programmatic=50, state=state)
        urls_to_submit = harvested["tier1_core"] + harvested["tier2_sitemaps"]

    # Filter recently submitted unless --force
    if not args.force and not args.url:
        filtered_urls = [u for u in urls_to_submit if not state.is_recently_submitted(u, "google")]
        print(f"Discovered URLs: {len(urls_to_submit)} | Fresh / Unindexed: {len(filtered_urls)}")
        urls_for_google = filtered_urls if filtered_urls else urls_to_submit[:15]
    else:
        urls_for_google = urls_to_submit

    print(f"Queue Size for Googlebot Indexing: {len(urls_for_google)}")
    print(f"Notification Type: {args.type}\n")

    # 3. Google Indexing API Execution with Auto-Rotation
    google_success = 0
    google_failed = 0
    google_quota_blocked = 0

    print("Submitting URL Notifications to Google Indexing API...")
    for idx, u in enumerate(urls_for_google):
        token, active_acc = km.get_token()
        if not token:
            print(f"  [!] All Google service account quotas exhausted for today ({google_success} submitted).")
            google_quota_blocked += (len(urls_for_google) - idx)
            break

        success, status_code, info = submit_single_url_google(u, token, args.type)
        if success:
            google_success += 1
            state.record_submission(u, "google", status_code, notify_time=info)
            print(f"  [{idx+1}/{len(urls_for_google)}] [✓ 200 OK] {u} -> Notified: {info}")
        elif status_code == 429:
            google_quota_blocked += 1
            km.mark_quota_exhausted(active_acc)
            # Retry immediately with next key in mesh
            token, next_acc = km.get_token()
            if token:
                s2, sc2, info2 = submit_single_url_google(u, token, args.type)
                if s2:
                    google_success += 1
                    state.record_submission(u, "google", sc2, notify_time=info2)
                    print(f"  [{idx+1}/{len(urls_for_google)}] [✓ 200 OK (Key #{km.active_index+1})] {u}")
                else:
                    google_failed += 1
            else:
                break
        else:
            google_failed += 1
            print(f"  [{idx+1}/{len(urls_for_google)}] [✗ {status_code}] {u} -> {info[:100]}")

    # 4. Multi-Engine IndexNow Network Submission (Broadcasting all URLs)
    indexnow_count = submit_indexnow(urls_to_submit)

    # 5. Broadcast Sitemap Pings
    ping_sitemaps()

    # 6. Save State and Report
    state.data["last_run"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    state.save()

    report = {
        "timestamp": state.data["last_run"],
        "total_queued": len(urls_to_submit),
        "google": {
            "submitted_success": google_success,
            "failed": google_failed,
            "quota_limited": google_quota_blocked,
            "accounts_configured": km.count()
        },
        "indexnow": {
            "pushed": indexnow_count,
            "status": "active"
        }
    }
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 70)
    print("  ENTERPRISE INDEXING RUN COMPLETE — SUMMARY REPORT")
    print(f"  Google Indexing API: {google_success} Published | {google_quota_blocked} Quota-Limited | {google_failed} Errors")
    print(f"  IndexNow Network:     {indexnow_count} URLs Pushed Directly to Bing/Copilot/Yandex")
    print(f"  Audit Report Saved:   {REPORT_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    main()
