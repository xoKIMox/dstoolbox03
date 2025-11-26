# Collect Thai Job Posting Data From Web Site

## Collection Project Information

website: 
    https://indeed.com

scraping tool:
    https://scrapy.org

## Job listing websites (curated)

Below is a curated list of job-listing sites grouped by scope/type. Use this as a starting point for scraping targets — check each site's robots.txt and Terms of Service before crawling.

### Global / Large aggregators
- Indeed (indeed.com)
- LinkedIn Jobs (linkedin.com/jobs)
- Glassdoor (glassdoor.com)
- Monster (monster.com)
- ZipRecruiter (ziprecruiter.com)
- CareerBuilder (careerbuilder.com)

### Tech / Developer-focused
- Dice (dice.com) — tech & engineering roles
- Hired (hired.com)
- Stack Overflow Jobs (changes over time — check current availability)
- Built In (builtinnetworks.com) — regional tech hubs (e.g., Built In Chicago)

### Remote / Startup / Startup-focused
- WeWorkRemotely (weworkremotely.com)
- Remote.co (remote.co)
- FlexJobs (flexjobs.com) — subscription service (note scraping restrictions)
- AngelList / Wellfound (wellfound.com) — startups & remote

### Gig / Freelance marketplaces
- Upwork (upwork.com)
- Freelancer (freelancer.com)

### Thailand / APAC-specific sites (useful for Thai job postings)
- JobThai (jobthai.com)
- JobsDB Thailand (th.jobsdb.com)
- JobBKK (jobbkk.com)
- ThaiJob (thaijob.com) / ThaiJobCenter
- JobsStreet / SEEK (jobsstreet.com / seek.com.au for APAC context)
- LinkedIn Thailand (region filter on LinkedIn Jobs)

### Country / Region-specific notable sites
- Naukri (naukri.com) — India
- InfoJobs / StepStone — Europe (country variants)
- SEEK (seek.com.au) — Australia & New Zealand
- Craigslist (jobs section) — localized regions (use with caution)

## Scraping notes and quick checklist
- robots.txt: Always check https://<site>/robots.txt. Respect crawl-delay and disallowed paths.
- Terms of service: Some sites (e.g., LinkedIn, Glassdoor) explicitly forbid scraping. Prefer official APIs or data partnerships.
- Rate limiting: Start very slow (1 request / 1–5s) and back off on HTTP 429 or connection errors.
- Identify pages to scrape: listing pages (search results, category pages), job detail pages, company pages.
- Common fields to extract:
	- job_id (if present)
	- title
	- company name
	- location (city, region, country)
	- posted date / age (e.g., "2 days ago")
	- salary (if available)
	- job description (HTML/text)
	- employment type (full-time/part-time/contract)
	- tags / skills
	- application url / external apply link
	- raw HTML / snapshot for downstream parsing
- Pagination patterns: numbered pages, "Load more" buttons (AJAX), or cursor/offset query params. Prefer using page parameters when available.
- Authentication / JS-rendered content: Some sites render listings via JavaScript; consider using a headless browser (Playwright / Puppeteer) judiciously and cache results.
- Data quality: Normalize dates, locations, and company names. Keep raw values for debugging.

## Example scraping contract (short)
- Inputs: start URL(s), optional search filters (keywords, location), page limit, rate-limit config.
- Outputs: CSV/JSONL with one job per record including scraped fields and source URL.
- Errors: log HTTP errors, parsing errors, and throttle events. Retry transient failures with exponential backoff.

## Legal & ethical note
This repo contains tooling to collect public job listing data for research or analytics. Make sure you have permission to scrape each target and follow local laws and the site's Terms of Service. When in doubt, use official APIs or ask for permission.

---

If you'd like, I can: add this as a dedicated `collect/job_sites.md` file instead, or convert the list into a CSV/JSON manifest used by your scrapers. Tell me which format you prefer.