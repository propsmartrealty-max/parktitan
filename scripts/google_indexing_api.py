#!/usr/bin/env python3
"""
Google Indexing API Batch Automation Script
For: purpleparktitan.com

Submits URL_UPDATED or URL_DELETED notifications directly to Googlebot
for immediate crawl & re-indexing within minutes.

Usage:
    python3 scripts/google_indexing_api.py --key service_account.json [--sitemap sitemaps/sitemap-pages.xml]
"""

import sys
import os
import json
import argparse
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    import requests
except ImportError:
    print("Error: Missing required packages. Run: pip install google-auth requests")
    sys.exit(1)

INDEXING_API_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

DEFAULT_URLS = [
    "https://purpleparktitan.com/",
    "https://purpleparktitan.com/videos/pride-purple-park-titan-official-walkthrough",
    "https://purpleparktitan.com/videos/",
    "https://purpleparktitan.com/explore/",
    "https://purpleparktitan.com/articles/",
    "https://purpleparktitan.com/articles/pride-purple-park-titan-hinjewadi-ecosystem-master-review.html",
    "https://purpleparktitan.com/articles/2bhk-3bhk-flats-hinjewadi-pune-market-guide.html",
    "https://purpleparktitan.com/articles/pune-real-estate-investment-rental-yields-hinjewadi.html",
    "https://purpleparktitan.com/articles/nri-guide-investing-in-pune-real-estate-park-titan.html",
    "https://purpleparktitan.com/articles/hinjewadi-metro-line-3-impact-on-pune-real-estate-property-rates.html"
]

def extract_urls_from_sitemap(sitemap_path):
    urls = []
    if not os.path.exists(sitemap_path):
        print(f"Warning: Sitemap {sitemap_path} not found.")
        return urls
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for loc in root.findall(".//sm:loc", namespace):
            if loc.text:
                urls.append(loc.text.strip())
        if not urls:
            # Fallback without namespace
            for loc in root.findall(".//loc"):
                if loc.text:
                    urls.append(loc.text.strip())
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
    return urls

def get_access_token(service_account_file):
    if not os.path.exists(service_account_file):
        print(f"\n[!] ERROR: Service Account key file not found: {service_account_file}")
        print("Please download your service_account.json from Google Cloud Console and place it in the project root.\n")
        return None
    try:
        credentials = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=SCOPES
        )
        credentials.refresh(Request())
        return credentials.token
    except Exception as e:
        print(f"Error authenticating with Service Account: {e}")
        return None

def publish_url(url, token, action_type="URL_UPDATED"):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "url": url,
        "type": action_type
    }
    try:
        res = requests.post(INDEXING_API_ENDPOINT, headers=headers, json=payload, timeout=15)
        if res.status_code == 200:
            data = res.json()
            time_str = data.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "Just now")
            print(f"  [✓ 200 OK] {url} -> Notified at {time_str}")
            return True
        else:
            print(f"  [✗ {res.status_code}] {url} -> {res.text}")
            return False
    except Exception as e:
        print(f"  [✗ ERROR] {url} -> {e}")
        return False


INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
INDEXNOW_KEY = "c7d094744fb02eb115c943afbffeb469"
INDEXNOW_KEY_LOCATION = "https://purpleparktitan.com/c7d094744fb02eb115c943afbffeb469.txt"

def submit_to_indexnow(urls):
    print("\n" + "=" * 65)
    print("  SUBMITTING TO INDEXNOW (BING, YANDEX, SEZNAM, NAVER, COPILOT)")
    print("=" * 65)
    payload = {
        "host": "purpleparktitan.com",
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": urls[:1000] # IndexNow allows up to 10,000 URLs per call
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    try:
        res = requests.post(INDEXNOW_ENDPOINT, headers=headers, json=payload, timeout=20)
        if res.status_code in [200, 202]:
            print(f"  [✓ {res.status_code} ACCEPTED] {len(urls)} URLs pushed directly to IndexNow network!")
            return True
        else:
            print(f"  [✗ {res.status_code}] IndexNow returned: {res.text}")
            return False
    except Exception as e:
        print(f"  [✗ ERROR] IndexNow submission error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Google Indexing API Batch Pushing Tool")
    parser.add_argument("--key", default="service_account.json", help="Path to Google Cloud Service Account JSON key")
    parser.add_argument("--sitemap", help="Optional path to XML sitemap to extract URLs from")
    parser.add_argument("--url", help="Single URL to index immediately")
    parser.add_argument("--type", default="URL_UPDATED", choices=["URL_UPDATED", "URL_DELETED"], help="Notification type")
    args = parser.parse_args()

    print("=" * 65)
    print("  GOOGLE INDEXING API AUTOMATION — PRIDE PURPLE PARK TITAN")
    print("=" * 65)

    token = get_access_token(args.key)
    if not token:
        sys.exit(1)

    urls_to_submit = []
    if args.url:
        urls_to_submit = [args.url]
    elif args.sitemap:
        urls_to_submit = extract_urls_from_sitemap(args.sitemap)
    else:
        urls_to_submit = DEFAULT_URLS

    print(f"Target URLs to push: {len(urls_to_submit)}")
    print(f"Action Type: {args.type}\n")

    success_count = 0
    for idx, u in enumerate(urls_to_submit):
        print(f"[{idx+1}/{len(urls_to_submit)}] Submitting to Googlebot...")
        if publish_url(u, token, args.type):
            success_count += 1

    print("\n" + "=" * 65)
    print(f"Completed! Submitted to Google Indexing API: {success_count}/{len(urls_to_submit)} successful.")
    if success_count == 0:
        print("  Notice: Google 200/day daily quota will reset at midnight PST.")

    # Push to IndexNow network (Bing, Yandex, Copilot)
    submit_to_indexnow(urls_to_submit)
    print("\n" + "=" * 65)
    print("MULTI-ENGINE INDEXING RUN COMPLETE!")
    print("=" * 65)

if __name__ == "__main__":
    main()
