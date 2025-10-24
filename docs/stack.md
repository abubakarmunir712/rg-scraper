# Research Genie — Scraping Tools, Languages & Data Sources

> **Goal:** Identify tools, languages, and target websites for scraping and data mining to collect full-text research papers and metadata for Research Genie.

---

## Tools & Languages for Scraping + Data Mining

**Primary languages**

* Python — ecosystem rich for scraping, parsing, NLP, and ML (requests/httpx, BeautifulSoup, Scrapy, Playwright, Pandas).
* JavaScript/TypeScript — for browser automation or Node-based scraping (Puppeteer, Playwright).

**Scraping libraries & frameworks**

* **Requests / httpx** — basic HTTP clients for fetching pages and APIs.
* **BeautifulSoup (bs4)** — simple HTML parsing and extraction.
* **Scrapy** — full-featured crawling framework (pipelines, throttling, exporters).
* **Playwright / Puppeteer / Selenium** — browser automation for JS-heavy sites.
* **newspaper3k** — fast article extraction for news-like pages (less useful for PDFs).

**Parsing / extraction / file handling**

* **PyPDF2 / pdfminer.six / tika** — extract text from PDFs.
* **Grobid** — parse scholarly PDFs into structured TEI XML (useful for sections: abstract, methods, refs).
* **pdfplumber** — precise PDF text/table extraction.

**Data processing / NLP / embeddings**

* **spaCy**, **NLTK** — tokenization, POS, NER.
* **SentenceTransformers** / OpenAI / Gemini embeddings — generate vectors for vector DB.
* **BERTopic / KeyBERT** — topic modelling & keyword extraction.

**Storage & infra**

* **MongoDB / PostgreSQL** — store metadata and raw text chunks.
* **Vector DBs:** Pinecone / Weaviate / FAISS — store embeddings for retrieval.
* **Message queues / task runners:** Celery + Redis, RabbitMQ, or FastAPI background tasks for jobs.
* **Containers & orchestration:** Docker, Kubernetes for scale.

**Legal & politeness tools**

* robots.txt parser libraries (e.g., `robotparser`), rate-limiters, exponential backoff, IP rotation via proxies (only if TOS allow).

---

## Websites to Scrape (Full-text / Open Access targets)

> Prioritize these for bulk/full-text harvesting. Prefer official APIs or bulk dumps when available.

1. **arXiv** — preprints (PDFs). Bulk + OAI-PMH available.
2. **bioRxiv** — life-science preprints (JSON endpoints / direct PDFs).
3. **medRxiv** — clinical/preprints (JSON endpoints).
4. **PubMed Central (PMC)** — full-text biomedical articles (XML/bulk).
5. **CORE.ac.uk** — aggregator of OA full-text papers (API + bulk dump).
6. **Institutional Repositories (University IRs)** — via OpenAlex/CORE discovery.
7. **PLOS** — fully OA journals (direct PDFs/API).
8. **Frontiers** — OA journals with JSON endpoints.
9. **MDPI** — OA journals; straightforward links to PDFs.
10. **SSRN** — social sciences preprints (mixed access; check TOS).
11. **OpenDOAR-hosted repositories** — various university archives.
12. **Zenodo** — OA articles, datasets, preprints (API + files).
13. **figshare** — datasets and sometimes full-texts connected to papers.
14. **Europe PMC** — alternative PMC mirror with APIs and full-text links.
15. **arXiv mirrors / Kaggle arXiv dataset** — bulk copies for large-scale experiments.
16. **Discipline-specific OA repositories** (e.g., RePEc for economics).

> *Notes:* Scrape these only for OA papers or where the repository permits crawling. Use OAI-PMH / bulk dumps when possible.

---

## Websites that Provide APIs (Prefer these over scraping)

> These endpoints give metadata and often full-text links or PDFs. Use API keys where required.

1. **OpenAlex API** — metadata + links to OA locations (good discovery layer).
2. **Unpaywall API** — locate legally free PDFs by DOI.
3. **Semantic Scholar API** — metadata + links to PDFs when available.
4. **CrossRef API** — authoritative metadata and DOIs (combine with Unpaywall to get PDFs).
5. **CORE API** — aggregated OA full-text content; bulk dumps available.
6. **arXiv API / OAI-PMH** — query and download preprints in bulk.
7. **PLOS API** — search & retrieve OA content.
8. **PMC / Europe PMC APIs** — full-text XML and metadata for biomedical literature.
9. **bioRxiv / medRxiv endpoints** — preprint JSON feeds.
10. **Zenodo API** — retrieve uploaded papers/datasets (OA).
11. **IEEE API** — metadata and content access (requires registration / subscription).
12. **DOAJ API** — directory of OA journals and articles.
13. **Microsoft Academic Graph replacement: OpenAlex** (listed above) — canonical replacement.

---

## Recommended Harvesting Strategy (short)

1. **Discovery**: Use OpenAlex + CrossRef to find DOIs and metadata for a domain.
2. **Full-text resolution**: For each DOI, query Unpaywall → if OA PDF found, download; else check CORE / arXiv / PMC.
3. **Bulk downloads**: Wherever possible, use arXiv bulk, CORE dumps, PMC bulk to reduce scraping pressure.
4. **Parsing**: Run Grobid on PDFs to extract structured sections.
5. **Indexing**: Embed sections and store in vector DB for RAG.

---

## Compliance & Ethics

* Always obey `robots.txt` and publisher TOS.
* Prefer APIs and bulk dumps.
* Log rate limits, errors, and take conservative download speeds.
* Attribute sources and respect license terms (e.g., CC-BY requirements).

---

## Next steps

* Draft FastAPI endpoints for orchestrating the discovery → resolution → download workflow.
* Create a Celery task queue for parallel downloads with rate limiting.
* Build a Grobid pipeline to parse and normalize full-text PDFs.

---

