# Google Search Console Registration & Indexing Guide

Follow these steps to submit `genedarocha.com` to **Google Search Console** (`console.google.com`) and rank at the top for AI & Web Development searches:

## Step 1: Add Property to Google Search Console
1. Navigate to [Google Search Console](https://search.google.com/search-console).
2. Click **Add Property**.
3. Select **Domain** (e.g. `genedarocha.com`) or **URL Prefix** (`https://genedarocha.com`).

## Step 2: Verify Domain Ownership
- **DNS TXT Record Method (Recommended for Domain Property)**:
  - Copy the TXT record provided by Google (e.g. `google-site-verification=...`).
  - Log into your DNS provider (Cloudflare, Namecheap, GoDaddy, Vercel, Netlify).
  - Add a TXT record for `@` with the value from Google.
- **HTML Meta Tag Method (For URL Prefix Property)**:
  - Copy the HTML meta tag: `<meta name="google-site-verification" content="..." />`.
  - Add it into the `<head>` section of `index.html`.

## Step 3: Submit Sitemap
1. Once verified, go to **Sitemaps** in the left sidebar menu.
2. In the **Add a new sitemap** field, enter:
   `sitemap.xml`
3. Click **Submit**.
4. Google will process your sitemap and begin crawling all new skill pages (`/skills/`, `/skills/ai-architecture.html`, `/skills/ai-development.html`, `/skills/ai-testing.html`).

## Step 4: Request Instant Indexing for Top Skill Pages
1. Use the **URL Inspection Tool** search bar at the top of Google Search Console.
2. Enter each of your key service URLs:
   - `https://genedarocha.com/skills/`
   - `https://genedarocha.com/skills/ai-testing.html`
   - `https://genedarocha.com/skills/ai-architecture.html`
   - `https://genedarocha.com/skills/ai-development.html`
3. Click **Request Indexing**. This places your pages in priority crawl queues.
