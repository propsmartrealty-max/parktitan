# Multi-Service Account Quota Multiplication Mesh

Google Cloud restricts the Google Indexing API to a default quota of **200 publish requests per day per project**.

To index at expansive enterprise scale (1,000 to 10,000+ URLs per day across the 13,000+ programmatic SEO corpus, floor plans, and research articles), simply drop additional Service Account JSON keys into this directory:

```
keys/
├── sa-project-1.json   # +200 URLs/day
├── sa-project-2.json   # +200 URLs/day
├── sa-project-3.json   # +200 URLs/day
├── sa-project-4.json   # +200 URLs/day
└── sa-project-5.json   # +200 URLs/day = 1,000 URLs/day total
```

### How It Works
1. `scripts/enterprise_indexer.py` automatically scans this folder upon startup.
2. It requests OAuth2 tokens for each active service account project.
3. When Project #1 hits the 200/day quota limit (`429 RESOURCE_EXHAUSTED`), the engine **seamlessly fails over to Project #2, #3, etc.** without interrupting the indexing run.
4. Each service account project must be added as a **Delegated Owner** in Google Search Console for `https://purpleparktitan.com/` (or Domain Property `purpleparktitan.com`).
