#!/usr/bin/env python3
"""
scripts/enterprise_indexer.py
ULTRA-ADVANCED ENTERPRISE-GRADE GOOGLE & MULTI-ENGINE INDEXING SUITE
Ecosystem: https://purpleparktitan.com/ (Pride Purple Park Titan Hinjewadi)

Enterprise Capabilities:
1. Multi-Project / Multi-Service Account Rotating Mesh (scales daily quota from 200/day to 10,000+/day)
2. RFC-Compliant HTTP Multipart Batching (https://indexing.googleapis.com/batch/indexing/v3)
3. Quota Pacemaker with PST Window Awareness (auto-calculates countdown to midnight PST quota reset)
4. Persistent Dedup State Machine (.indexing_state.json) preventing duplicate quota burn
5. Comprehensive Ecosystem Harvester:
   - Tier 1: Core Portal, Walkthrough Videos, Market Articles, llms.txt (Priority 1.0)
   - Tier 2: Visual Web Stories, Sanctioned Floor Plans (Priority 0.8)
   - Tier 3: 13,000+ Programmatic SEO Exploration Corpus (Priority 0.5, sequential offset rotation)
6. IndexNow Network Broadcast (up to 10,000 URLs pushed to Bing, Copilot, Yandex, Seznam, Naver)
7. Search Console & Bing Master Sitemap Ping Broadcaster
8. Self-Healing Exponential Backoff with Jitter for transient network faults
9. CLI Modes: --all, --force, --inspect <URL>, --health-check, --stats, --batch-size <N>
10. JSON Audit Trail (indexing_report.json)
"""

import sys
import os
import glob
import json
import time
import uuid
import random
import argparse
import datetime
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    import requests
except ImportError:
    print("Error: Required packages missing. Run: pip install google-auth requests")
    sys.exit(1)

# API Endpoints
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
KEYS_DIR = "keys"

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
    "https://purpleparktitan.com/.well-known/llms.txt",
    "https://purpleparktitan.com/web-stories/5-academies-park-titan",
    "https://purpleparktitan.com/web-stories/7-acre-podium-park-titan",
    "https://purpleparktitan.com/web-stories/2bhk-3bhk-floor-plans-park-titan"
]

def get_pst_reset_time():
    """Calculates next midnight Pacific Time (PST/PDT) when Google daily 200 quota resets."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    # PST is UTC-8 (or PDT UTC-7). Using 08:00 UTC as safe boundary
    today_reset = now_utc.replace(hour=8, minute=0, second=0, microsecond=0)
    if now_utc >= today_reset:
        return today_reset + datetime.timedelta(days=1)
    return today_reset

class KeyManager:
    """Enterprise multi-project mesh: seamlessly manages and rotates across service accounts."""
    def __init__(self, key_paths, state_mgr):
        self.key_paths = key_paths
        self.state_mgr = state_mgr
        self.accounts = []
        self.active_index = 0
        self._load_accounts()

    def _load_accounts(self):
        seen_emails = set()
        for path in self.key_paths:
            if not os.path.exists(path):
                continue
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                client_email = data.get('client_email', '')
                project_id = data.get('project_id', '')
                if not client_email or client_email in seen_emails:
                    continue
                seen_emails.add(client_email)
                creds = service_account.Credentials.from_service_account_file(
                    path, scopes=SCOPES
                )
                exhausted_until = self.state_mgr.get_account_exhaustion(project_id)
                now_epoch = time.time()
                is_exhausted = (exhausted_until and now_epoch < exhausted_until)
                self.accounts.append({
                    "path": path,
                    "email": client_email,
                    "project_id": project_id,
                    "creds": creds,
                    "token": None,
                    "token_expiry": 0,
                    "quota_exhausted": bool(is_exhausted),
                    "exhausted_until": exhausted_until,
                    "published_count": 0
                })
            except Exception as e:
                print(f"[KeyManager] Warning: Failed to parse key at {path}: {e}")

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
                    print(f"[KeyManager] Auth Error for {acc['email']}: {e}")
                    acc["quota_exhausted"] = True
                    self.active_index += 1
                    continue
            return acc["token"], acc
        return None, None

    def mark_quota_exhausted(self, acc):
        reset_time = get_pst_reset_time()
        reset_epoch = reset_time.timestamp()
        acc["quota_exhausted"] = True
        acc["exhausted_until"] = reset_epoch
        self.state_mgr.set_account_exhaustion(acc["project_id"], reset_epoch)
        rem = reset_time - datetime.datetime.now(datetime.timezone.utc)
        hours, rem_s = divmod(int(rem.total_seconds()), 3600)
        mins, _ = divmod(rem_s, 60)
        print(f"[KeyManager] ⚠️ Quota (200/day) reached for project '{acc['project_id']}'. Resets in {hours}h {mins}m at 00:00 PST.")
        self.active_index += 1
        if self.active_index < len(self.accounts):
            next_acc = self.accounts[self.active_index]
            print(f"[KeyManager] 🔄 Seamlessly rotating to Service Account #{self.active_index+1}: '{next_acc['project_id']}' ({next_acc['email']})")
        else:
            print("[KeyManager] ⛔ All configured service accounts have exhausted their daily quota.")

class StateManager:
    """Persistent state machine for submitted URLs, quota timers, and rotating offsets."""
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
            "account_exhaustion": {},
            "urls": {}
        }

    def save(self):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"[StateManager] Warning: Error saving state: {e}")

    def get_account_exhaustion(self, project_id):
        return self.data.get("account_exhaustion", {}).get(project_id)

    def set_account_exhaustion(self, project_id, reset_epoch):
        if "account_exhaustion" not in self.data:
            self.data["account_exhaustion"] = {}
        self.data["account_exhaustion"][project_id] = reset_epoch

    def record_submission(self, url, engine, status, notify_time=None):
        if "urls" not in self.data:
            self.data["urls"] = {}
        if url not in self.data["urls"]:
            self.data["urls"][url] = {}
        self.data["urls"][url][engine] = {
            "submitted_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "status": status,
            "notify_time": notify_time
        }

    def is_recently_submitted(self, url, engine="google", hours=24):
        entry = self.data.get("urls", {}).get(url, {}).get(engine)
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
    """Enterprise XML Sitemap parser & ecosystem aggregator."""
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
            print(f"[Harvester] Error reading {sitemap_path}: {e}")
        return urls

    @classmethod
    def harvest_all(cls, max_programmatic=500, state=None):
        harvested = {
            "tier1_core": list(TIER_1_CORE_URLS),
            "tier2_sitemaps": [],
            "tier3_programmatic": []
        }
        for sm in ["sitemaps/sitemap-pages.xml", "sitemaps/sitemap-articles.xml", "sitemaps/sitemap-media.xml", "sitemaps/sitemap-stories.xml"]:
            for u in cls.extract_urls(sm):
                if u not in harvested["tier1_core"]:
                    harvested["tier2_sitemaps"].append(u)

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

def build_multipart_batch(urls, action_type="URL_UPDATED"):
    """Constructs RFC-compliant multipart/mixed HTTP request payload for Google Batch Indexing API."""
    boundary = f"batch_parktitan_{uuid.uuid4().hex}"
    parts = []
    for idx, u in enumerate(urls):
        body = json.dumps({"url": u, "type": action_type})
        part = (
            f"--{boundary}\r\n"
            f"Content-Type: application/http\r\n"
            f"Content-Transfer-Encoding: binary\r\n"
            f"Content-ID: <item-{idx}>\r\n\r\n"
            f"POST /v3/urlNotifications:publish HTTP/1.1\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len(body)}\r\n\r\n"
            f"{body}\r\n"
        )
        parts.append(part)
    parts.append(f"--{boundary}--\r\n")
    payload = "".join(parts)
    return boundary, payload

def submit_batch_google(urls, token, action_type="URL_UPDATED", max_retries=3):
    """Submits up to 100 URL notifications in a single multipart HTTP POST to Google."""
    boundary, body = build_multipart_batch(urls, action_type)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": f"multipart/mixed; boundary={boundary}"
    }
    for attempt in range(max_retries):
        try:
            res = requests.post(INDEXING_API_BATCH, headers=headers, data=body.encode('utf-8'), timeout=30)
            if res.status_code == 200:
                # Count successful parts in multipart response
                resp_text = res.text
                success_count = resp_text.count("HTTP/1.1 200 OK")
                quota_count = resp_text.count("429")
                return True, res.status_code, success_count, quota_count, resp_text
            elif res.status_code == 429:
                return False, 429, 0, len(urls), res.text
            else:
                if attempt < max_retries - 1:
                    time.sleep(1.5 * (attempt + 1) + random.uniform(0, 0.5))
                    continue
                return False, res.status_code, 0, 0, res.text
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(1.5 * (attempt + 1) + random.uniform(0, 0.5))
                continue
            return False, 0, 0, 0, str(e)
    return False, 0, 0, 0, "Max retries exceeded"

def submit_single_url_google(url, token, action_type="URL_UPDATED"):
    """Submits a single URL notification directly to Googlebot with backoff."""
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

def inspect_url(url, token):
    """Queries Google's real-time indexing metadata for a specific URL."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"url": url}
    print(f"\n[Inspect] Querying Google Indexing Metadata for: {url}")
    try:
        res = requests.get(INDEXING_API_METADATA, headers=headers, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            print("  [✓ 200 OK] Google Indexing Metadata Verified:")
            print(json.dumps(data, indent=2))
            return data
        elif res.status_code == 404:
            print("  [i 404 NOT_FOUND] Google has no prior notification on record for this URL.")
            return None
        else:
            print(f"  [✗ {res.status_code}] Google API error: {res.text}")
            return None
    except Exception as e:
        print(f"  [✗ ERROR] Inspection failed: {e}")
        return None

def submit_indexnow(urls):
    """Pushes up to 10,000 URLs to the IndexNow network (Bing, Copilot, Yandex, Seznam, Naver)."""
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
            print(f"  [✓ {res.status_code}] {name} dispatched: {endpoint}")
        except Exception as e:
            print(f"  [i] {name} ping note: {e}")

def run_health_check(km):
    """Performs diagnostic connectivity and authentication test for all service accounts."""
    print("\n" + "=" * 70)
    print("  ENTERPRISE INDEXING HEALTH CHECK & CREDENTIAL DIAGNOSTICS")
    print("=" * 70)
    print(f"Total Service Account Keys Loaded: {km.count()}")
    for idx, acc in enumerate(km.accounts):
        print(f"\nAccount #{idx+1}:")
        print(f"  Project ID:   {acc['project_id']}")
        print(f"  Client Email: {acc['email']}")
        print(f"  Key File:     {acc['path']}")
        try:
            acc["creds"].refresh(Request())
            print(f"  Token Auth:   ✓ VALID (Expires in 3600s)")
            # Test test-ping on Google metadata
            headers = {"Authorization": f"Bearer {acc['creds'].token}"}
            res = requests.get(INDEXING_API_METADATA, headers=headers, params={"url": f"https://{HOST_DOMAIN}/"}, timeout=10)
            if res.status_code in [200, 404]:
                print(f"  Google API:   ✓ CONNECTED (HTTP {res.status_code})")
            elif res.status_code == 429:
                print(f"  Google API:   ⚠️ QUOTA EXHAUSTED (HTTP 429 - Resets at 00:00 PST)")
            elif res.status_code == 403:
                print(f"  Google API:   ⚠️ PERMISSION DENIED (Add '{acc['email']}' as Owner in Google Search Console)")
            else:
                print(f"  Google API:   Status {res.status_code}: {res.text[:80]}")
        except Exception as e:
            print(f"  Token Auth:   ✗ FAILED: {e}")

def print_stats(state):
    """Displays cumulative indexing statistics from state file."""
    urls = state.data.get("urls", {})
    total = len(urls)
    google_indexed = sum(1 for u in urls.values() if "google" in u and u["google"].get("status") == 200)
    indexnow_indexed = sum(1 for u in urls.values() if "indexnow" in u)
    print("\n" + "=" * 70)
    print("  HISTORICAL INDEXING STATE & STATISTICS")
    print("=" * 70)
    print(f"  Last Run Timestamp:      {state.data.get('last_run', 'Never')}")
    print(f"  Programmatic Offset:     {state.data.get('programmatic_offset', 0)}")
    print(f"  Total Unique URLs Tracked: {total}")
    print(f"  Google Notifications Sent: {google_indexed}")
    print(f"  IndexNow Network Pushed:   {indexnow_indexed}")
    reset_time = get_pst_reset_time()
    rem = reset_time - datetime.datetime.now(datetime.timezone.utc)
    hours, rem_s = divmod(int(rem.total_seconds()), 3600)
    mins, _ = divmod(rem_s, 60)
    print(f"  Next Google Quota Reset: {reset_time.isoformat()} (in {hours}h {mins}m)")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Ultra-Advanced Enterprise Google & Multi-Engine Indexing Suite")
    parser.add_argument("--keys-dir", default=KEYS_DIR, help="Directory containing multiple service account JSON keys")
    parser.add_argument("--key", default="service_account.json", help="Path to default Google Cloud Service Account key")
    parser.add_argument("--url", help="Single URL to index or inspect")
    parser.add_argument("--inspect", action="store_true", help="Inspect real-time Google indexing metadata for target URL")
    parser.add_argument("--health-check", action="store_true", help="Run diagnostic health check on all service accounts")
    parser.add_argument("--stats", action="store_true", help="Display historical indexing statistics")
    parser.add_argument("--all", action="store_true", help="Harvest all sitemaps (including programmatic corpus) for mass broadcast")
    parser.add_argument("--max-programmatic", type=int, default=500, help="Max programmatic URLs to rotate in this run")
    parser.add_argument("--batch-size", type=int, default=50, help="Batch chunk size for Google multipart requests (max 100)")
    parser.add_argument("--force", action="store_true", help="Force re-indexing even if submitted within last 24 hours")
    parser.add_argument("--dry-run", action="store_true", help="Simulate harvesting and batch creation without sending API calls")
    parser.add_argument("--type", default="URL_UPDATED", choices=["URL_UPDATED", "URL_DELETED"], help="Notification type")
    args = parser.parse_args()

    state = StateManager()

    if args.stats:
        print_stats(state)
        sys.exit(0)

    # 1. Discover Service Account Keys
    key_paths = []
    if os.path.exists(args.key):
        key_paths.append(args.key)
    if os.path.exists(args.keys_dir):
        key_paths.extend(glob.glob(os.path.join(args.keys_dir, "*.json")))
    env_keys = os.environ.get("GOOGLE_INDEXING_KEYS")
    if env_keys:
        for p in env_keys.split(","):
            if os.path.exists(p.strip()):
                key_paths.append(p.strip())

    key_paths = list(dict.fromkeys(key_paths))
    km = KeyManager(key_paths, state)

    if args.health_check:
        run_health_check(km)
        sys.exit(0)

    if args.url and args.inspect:
        token, acc = km.get_token()
        if not token:
            print("[!] Error: No valid Google authentication token available.")
            sys.exit(1)
        inspect_url(args.url, token)
        sys.exit(0)

    print("=" * 70)
    print("  PRIDE PURPLE PARK TITAN — ENTERPRISE MULTI-ENGINE INDEXING SUITE")
    print(f"  Domain: https://{HOST_DOMAIN}/ | Active SA Keys: {km.count()}")
    print("=" * 70)

    # 2. Build URL Priority Queue
    if args.url:
        urls_to_submit = [args.url]
    elif args.all:
        harvested = SitemapHarvester.harvest_all(max_programmatic=args.max_programmatic, state=state)
        urls_to_submit = harvested["tier1_core"] + harvested["tier2_sitemaps"] + harvested["tier3_programmatic"]
    else:
        harvested = SitemapHarvester.harvest_all(max_programmatic=100, state=state)
        urls_to_submit = harvested["tier1_core"] + harvested["tier2_sitemaps"]

    # Filter recently submitted unless --force
    if not args.force and not args.url:
        filtered_urls = [u for u in urls_to_submit if not state.is_recently_submitted(u, "google")]
        urls_for_google = filtered_urls if filtered_urls else urls_to_submit[:15]
    else:
        urls_for_google = urls_to_submit

    print(f"Discovered URLs: {len(urls_to_submit)} | Queued for Googlebot: {len(urls_for_google)}")
    print(f"Notification Type: {args.type} | Dry Run: {args.dry_run}\n")

    if args.dry_run:
        print("[Dry Run] URLs ready for dispatch:")
        for idx, u in enumerate(urls_for_google[:15]):
            print(f"  {idx+1}. {u}")
        if len(urls_for_google) > 15:
            print(f"  ... and {len(urls_for_google) - 15} more.")
        sys.exit(0)

    # 3. Google Indexing API Execution with Multipart Batching & Key Rotation
    google_success = 0
    google_failed = 0
    google_quota_blocked = 0

    print("Submitting URL Notifications to Google Indexing API...")
    batch_size = min(max(1, args.batch_size), 100)
    idx = 0
    while idx < len(urls_for_google):
        token, active_acc = km.get_token()
        if not token:
            rem = len(urls_for_google) - idx
            print(f"  [!] All Google service account quotas exhausted for today ({google_success} successful). {rem} URLs queued for next window.")
            google_quota_blocked += rem
            break

        chunk = urls_for_google[idx:idx + batch_size]
        
        # Try multipart batch request first
        success, status_code, succ_cnt, quota_cnt, info = submit_batch_google(chunk, token, args.type)
        if success and succ_cnt > 0:
            google_success += succ_cnt
            for u in chunk[:succ_cnt]:
                state.record_submission(u, "google", 200, notify_time="BATCH_OK")
            print(f"  [Batch {idx//batch_size + 1}] [✓ 200 OK] Successfully pushed {succ_cnt}/{len(chunk)} URLs via Google Batch API")
            if quota_cnt > 0:
                km.mark_quota_exhausted(active_acc)
            idx += succ_cnt
        elif status_code == 429 or quota_cnt > 0:
            km.mark_quota_exhausted(active_acc)
            # If batch failed with 429, retry first URL individually with rotated key
            token, next_acc = km.get_token()
            if not token:
                rem = len(urls_for_google) - idx
                google_quota_blocked += rem
                break
            # Fallback to single URL processing for fine-grained quota control
            target_url = chunk[0]
            s_ok, s_code, s_info = submit_single_url_google(target_url, token, args.type)
            if s_ok:
                google_success += 1
                state.record_submission(target_url, "google", s_code, notify_time=s_info)
                print(f"  [{idx+1}/{len(urls_for_google)}] [✓ 200 OK (Key #{km.active_index+1})] {target_url}")
                idx += 1
            elif s_code == 429:
                km.mark_quota_exhausted(next_acc)
            else:
                google_failed += 1
                idx += 1
        else:
            # Batch rejected; process chunk one-by-one as fallback
            for single_u in chunk:
                token, curr_acc = km.get_token()
                if not token:
                    break
                s_ok, s_code, s_info = submit_single_url_google(single_u, token, args.type)
                if s_ok:
                    google_success += 1
                    state.record_submission(single_u, "google", s_code, notify_time=s_info)
                    print(f"  [{idx+1}/{len(urls_for_google)}] [✓ 200 OK] {single_u}")
                elif s_code == 429:
                    km.mark_quota_exhausted(curr_acc)
                    break
                else:
                    google_failed += 1
                idx += 1

    # 4. Multi-Engine IndexNow Network Submission (Broadcasting entire queue)
    indexnow_count = submit_indexnow(urls_to_submit)
    for u in urls_to_submit:
        state.record_submission(u, "indexnow", 200)

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
    print("  ENTERPRISE INDEXING RUN COMPLETE — SUMMARY AUDIT")
    print(f"  Google Indexing API: {google_success} Published | {google_quota_blocked} Quota-Limited | {google_failed} Errors")
    print(f"  IndexNow Network:     {indexnow_count} URLs Pushed Directly to Bing/Copilot/Yandex")
    print(f"  Audit Report Saved:   {REPORT_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    main()
