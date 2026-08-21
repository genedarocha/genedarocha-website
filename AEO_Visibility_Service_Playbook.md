# Voxstar AI Visibility & AEO (Answer Engine Optimization) Service Playbook

## 🚀 Overview: The Shift from SEO to AEO
Traditional Search Engine Optimization (SEO) focused on getting blue link clicks on Google. 
**Answer Engine Optimization (AEO)** is the modern discipline of positioning a business or founder as the authoritative, cited source inside Conversational AI models like **ChatGPT, Google Gemini, Anthropic Claude, Perplexity AI, and Microsoft Copilot**.

When users ask LLMs: *"Who is the best AI Architect in the UK?"* or *"What company provides zero-trust AI security proxies?"*, AI engines don't crawl the entire web dynamically. They rely on **knowledge graph entities**, **JSON-LD structured data**, **FAQ answer readiness**, and **canonical verification**.

---

## 🔍 The 5 Pillars of AEO (What Scanners & LLMs Look For)

```
                       ┌─────────────────────────────────────────┐
                       │      AI ANSWER ENGINE VISIBILITY        │
                       └───────────────────┬─────────────────────┘
                                           │
       ┌───────────────────┬───────────────┴───────────────┬───────────────────┐
       ▼                   ▼                               ▼                   ▼
┌──────────────┐    ┌──────────────┐                ┌──────────────┐    ┌──────────────┐
│  STRUCTURED  │    │    ANSWER    │                │    ENTITY    │    │  CRAWL & MAP │
│     DATA     │    │  READINESS   │                │ UNDERSTAND   │    │  DISCOVERY   │
│  (JSON-LD)   │    │  (FAQ SCHEMA)│                │  (sameAs Graph│    │(Sitemaps/Rob)│
└──────────────┘    └──────────────┘                └──────────────┘    └──────────────┘
```

### 1. Structured Data (JSON-LD Schema) — Weight: High
- Without Schema, LLMs infer data probabilistically (unreliable).
- With Schema (`@type: Organization`, `@type: Person`, `@type: WebSite`, `@type: FAQPage`), you provide explicit, deterministic facts.
- **Key Fields**: `@id`, `name`, `legalName`, `alternateName`, `url`, `logo`, `founder`, `contactPoint`.

### 2. Answer Readiness & FAQ Content — Weight: High
- AI Answer Engines extract direct QA blocks.
- **Requirement**: A dedicated, crawlable FAQ section wrapped in `FAQPage` JSON-LD schema with concise answers (30–60 words) to "Who", "What", "How", and "Pricing/Services".

### 3. Entity Understanding & Entity Resolution — Weight: Medium
- Linking domain aliases (`genedarocha.com`, `www.genedarocha.com`, `voxstar.com`) and social profiles (`LinkedIn`, `GitHub`, `Substack`, `Spotify`, `Wikipedia`) in the `sameAs` schema array.
- This creates an indisputable entity record across search engine graphs.

### 4. AI Crawlability & Sitemaps — Weight: Low/Medium
- Ensuring `robots.txt` explicitly allows AI bots (`User-agent: * Allow: /`).
- Including `<link rel="sitemap" href="/sitemap.xml">` in all `<head>` sections.

### 5. Citation Confidence & Canonical Anchoring — Weight: High
- Explicit `<link rel="canonical" href="...">` tags prevent duplicate content confusion.
- Clear heading hierarchy (`<h1>` per page, semantic `<h2>`, `<h3>`).

---

## 🛠️ Step-by-Step: What We Implemented on `genedarocha.com`

1. **Dual Domain & Entity Linking**:
   - Linked `genedarocha.com` and `www.genedarocha.com` in `alternateName` and `sameAs` schema arrays.
   - Connected `Voxstar Ltd` as the parent organization and `Gene Da Rocha` as the founder/person entity.

2. **Homepage FAQ Answer Engine Module**:
   - Implemented an interactive CSS/JS FAQ Accordion on `index.html` answering the top 5 questions answer engines look for.
   - Dual-embedded matching `FAQPage` JSON-LD schema.

3. **Complete Metadata Infrastructure**:
   - Added missing `<meta name="description">` and `<link rel="canonical">` to all pages.
   - Generated XML sitemap (`sitemap.xml`) and `robots.txt`.
   - Added `<link rel="sitemap">` head tag.

4. **Internal Link Graph**:
   - Created crawlable text navigation links between main page, skills overview hub, AI architecture, AI development, and AI testing pages.

---

## 📊 Client Case Study & Proof Evidence (`genedarocha.com` Benchmark)

Use this real-world before-and-after audit benchmark in client proposals to demonstrate the quantifiable ROI of Voxstar's AEO Optimization service.

### Benchmark Transformation Matrix (Omni Impact AEO Scanner)

| AEO Audit Metric | Initial Baseline (Grade D) | Post-Voxstar Optimization (Grade A+) | Impact & Delta |
|---|---|---|---|
| **Overall AEO Score** | 🔴 **56 / 100** | 🟢 **98 / 100** | 🚀 **+42 Points (Grade D ➔ Grade A+)** |
| **Structured Data** | 🔴 **10 / 100** | 🟢 **100 / 100** | 📈 **+90 Points** (Added WebSite, Org, Person, FAQPage schemas) |
| **Entity Understanding** | 🟠 **56 / 100** | 🟢 **98 / 100** | 📈 **+42 Points** (Linked domain aliases & social entity graph) |
| **Answer Readiness** | 🟠 **73 / 100** | 🟢 **98 / 100** | 📈 **+25 Points** (Added FAQ module & FAQPage schema) |
| **AI Crawlability** | 🟢 **77 / 100** | 🟢 **100 / 100** | 📈 **+23 Points** (Added sitemap.xml & robots.txt) |
| **Citation Confidence** | 🟢 **82 / 100** | 🟢 **98 / 100** | 📈 **+16 Points** (Added canonical tags & meta descriptions) |

### 📋 Checklist Audit Proof

| Signal Tested | Initial Scan | Post-Optimization Status | Voxstar Technical Action |
|---|---|---|---|
| **Organization or WebSite Schema** | ❌ **FAIL** | ✅ **PASS** | Added `@type: Organization` (Voxstar Ltd) and `@type: WebSite` |
| **Content-Level Schema** | ❌ **FAIL** | ✅ **PASS** | Added `@type: Service` and `@type: FAQPage` |
| **Meta Description Present** | ❌ **FAIL** | ✅ **PASS** | Added high-impact meta description tags |
| **Canonical URL Set** | ❌ **FAIL** | ✅ **PASS** | Added `<link rel="canonical">` to all pages |
| **FAQ / Help Content Found** | ❌ **FAIL** | ✅ **PASS** | Designed on-page FAQ accordion module |
| **Sitemap Discoverable** | ❌ **FAIL** | ✅ **PASS** | Created `sitemap.xml` and `<link rel="sitemap">` head tags |
| **Internal Link Graph** | ❌ **FAIL** | ✅ **PASS** | Added crawlable HTML text navigation links |

---

## 💼 How Voxstar Packages & Sells AEO as a High-Ticket Client Service

### Service Name: **Voxstar AI Visibility & AEO Optimization Package**
**Price Point**: £2,500 – £7,500 one-off audit & implementation (or £1,000/mo retainer)

### Client Sales Pitch:
> *"Is your brand visible when potential customers ask ChatGPT, Gemini, or Perplexity for recommendations in your industry? Most websites score under 60/100 on AI Answer Engine Readiness. Voxstar optimizes your digital presence so AI answer engines recommend and cite your business as the top authority."*

### Deliverables Package:
1. **Initial AEO Baseline Audit**: Run AEO scanner check to establish initial score (e.g., 56/100 Grade D).
2. **Multi-Entity Schema Architecture**: Write custom JSON-LD graphs for Organization, Founders, Products, Services, and FAQPages.
3. **On-Page Answer Engine Content Optimization**: Design & embed high-converting FAQ modules.
4. **AI Crawl & Indexation Setup**: Sitemap generation, `robots.txt` optimization, and Search Console submission.
5. **Re-Scan Verification & Certificate**: Deliver post-optimization report showing the jump to **95–100/100 Grade A+**.
