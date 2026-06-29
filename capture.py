"""Capture full-page screenshots and discover internal links for 3 Serbian brokerage competitors."""
import asyncio
import json
import re
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path("/Users/ogurianova/Desktop/TESLA/competitive-analysis")
SHOTS = ROOT / "screenshots"

COMPETITORS = [
    {
        "key": "ilirika",
        "name": "Ilirika investments a.d., Beograd",
        "url": "https://ilirika.rs/",
    },
    {
        "key": "momentum",
        "name": "Momentum Securities a.d., Novi Sad",
        "url": "https://momentum.rs/",
    },
    {
        "key": "prudence",
        "name": "Prudence Capital a.d., Beograd",
        "url": "https://prudencecapital.rs/",
    },
]

# Keywords (Serbian + English) used to discover internal pages we care about
PAGE_TARGETS = {
    "services": [
        r"uslug", r"servis", r"brokersk", r"trgov", r"investicij",
        r"service", r"product",
    ],
    "portfolio": [
        r"portfolio", r"portfeli", r"upravljan", r"portfolio.management",
        r"asset.management", r"wealth",
    ],
    "education_news": [
        r"vest", r"novost", r"blog", r"edukacij", r"analiz", r"istraziv",
        r"news", r"insight", r"research", r"education", r"learn",
    ],
    "contact": [
        r"kontakt", r"contact", r"otvar", r"otvori.racun", r"open.account",
        r"prijava", r"registracij",
    ],
    "about": [
        r"o.nama", r"o-nama", r"about", r"company", r"kompanij",
    ],
    "fees": [
        r"tarif", r"naknad", r"cen", r"fee", r"price", r"pricing",
    ],
}


async def discover_links(page, base_url):
    """Pull internal links categorized by target purpose."""
    links = await page.eval_on_selector_all(
        "a[href]",
        "els => els.map(e => ({href: e.href, text: (e.innerText||'').trim().slice(0,80)}))",
    )
    base_host = re.sub(r"^https?://", "", base_url).split("/")[0]
    cats = {k: [] for k in PAGE_TARGETS}
    seen = set()
    for l in links:
        href = l["href"]
        if not href.startswith("http"):
            continue
        host = re.sub(r"^https?://", "", href).split("/")[0]
        if base_host.replace("www.", "") not in host.replace("www.", ""):
            continue
        if href in seen:
            continue
        seen.add(href)
        text = l["text"].lower()
        path = href.lower()
        for cat, patterns in PAGE_TARGETS.items():
            for p in patterns:
                if re.search(p, path) or re.search(p, text):
                    if href not in cats[cat]:
                        cats[cat].append({"href": href, "text": l["text"]})
                    break
    return cats


async def safe_screenshot(page, path, full_page=True):
    try:
        await page.screenshot(path=str(path), full_page=full_page)
        return True
    except Exception as e:
        print(f"  ! screenshot failed for {path.name}: {e}")
        return False


async def safe_goto(page, url, wait=2500):
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
    except Exception:
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            print(f"  ! goto failed: {url} -> {e}")
            return False
    # Try to dismiss cookie banners
    for sel in [
        "button:has-text('Prihvatam')", "button:has-text('Prihvati')",
        "button:has-text('Accept')", "button:has-text('OK')",
        "button:has-text('Slažem se')", "button:has-text('Saglasan')",
        "#onetrust-accept-btn-handler", ".cookie-accept",
        "button[aria-label*='ccept']",
    ]:
        try:
            btn = await page.query_selector(sel)
            if btn:
                await btn.click(timeout=1500)
                await page.wait_for_timeout(500)
                break
        except Exception:
            pass
    await page.wait_for_timeout(wait)
    # Scroll to trigger lazy-loaded assets
    try:
        await page.evaluate(
            "async () => { const d = document.body.scrollHeight; "
            "for (let y=0; y<d; y+=600) { window.scrollTo(0,y); "
            "await new Promise(r=>setTimeout(r,80)); } "
            "window.scrollTo(0,0); }"
        )
    except Exception:
        pass
    await page.wait_for_timeout(800)
    return True


async def capture_one(browser, comp):
    print(f"\n=== {comp['name']} ===")
    out = SHOTS / comp["key"]
    out.mkdir(parents=True, exist_ok=True)
    summary = {"name": comp["name"], "url": comp["url"], "pages": {}}

    ctx = await browser.new_context(
        viewport={"width": 1440, "height": 900},
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="sr-RS",
    )
    page = await ctx.new_page()

    # Home
    ok = await safe_goto(page, comp["url"])
    if ok:
        await safe_screenshot(page, out / "01-home.png")
        title = await page.title()
        meta_desc = await page.evaluate(
            "() => (document.querySelector('meta[name=description]')||{}).content || ''"
        )
        body_text = await page.evaluate(
            "() => document.body.innerText.slice(0, 6000)"
        )
        nav_text = await page.evaluate(
            "() => Array.from(document.querySelectorAll('nav a, header a'))"
            ".map(a=>a.innerText.trim()).filter(t=>t).slice(0,40).join(' | ')"
        )
        summary["pages"]["home"] = {
            "url": comp["url"],
            "title": title,
            "meta_description": meta_desc,
            "nav_text": nav_text,
            "body_text": body_text,
        }
        cats = await discover_links(page, comp["url"])
        summary["discovered_links"] = cats

        # Visit one URL per category we care about (services, portfolio, edu, contact, about, fees)
        visited = set([comp["url"].rstrip("/")])
        for cat, items in cats.items():
            for it in items[:1]:  # top match per category
                target = it["href"]
                if target.rstrip("/") in visited:
                    continue
                visited.add(target.rstrip("/"))
                fname = f"02-{cat}.png" if cat == "services" else \
                        f"03-{cat}.png" if cat == "portfolio" else \
                        f"04-{cat}.png" if cat == "education_news" else \
                        f"05-{cat}.png" if cat == "contact" else \
                        f"06-{cat}.png" if cat == "about" else \
                        f"07-{cat}.png"
                print(f"  -> {cat}: {target}")
                ok2 = await safe_goto(page, target)
                if ok2:
                    await safe_screenshot(page, out / fname)
                    try:
                        ptitle = await page.title()
                        ptext = await page.evaluate(
                            "() => document.body.innerText.slice(0,4500)"
                        )
                    except Exception:
                        ptitle, ptext = "", ""
                    summary["pages"][cat] = {
                        "url": target,
                        "title": ptitle,
                        "body_text": ptext,
                    }
                break

    await ctx.close()
    return summary


async def main():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for comp in COMPETITORS:
            try:
                res = await capture_one(browser, comp)
                results.append(res)
            except Exception as e:
                print(f"FATAL on {comp['key']}: {e}")
                results.append({"name": comp["name"], "url": comp["url"], "error": str(e)})
        await browser.close()
    (ROOT / "raw_data.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print("\nDone. Raw data -> raw_data.json")


if __name__ == "__main__":
    asyncio.run(main())
