# Competitive Analysis — Serbian Brokerage Market

**Client:** Tesla Capital a.d., Beograd (brokerage, securities trading, investment advisory, portfolio management — 25+ years on the Serbian market)
**Date of capture:** 27 May 2026
**Method:** Headless-Chromium (Playwright) full-page captures + DOM/text extraction.
**Competitors reviewed:**
1. Ilirika investments a.d., Beograd — https://ilirika.rs/
2. Momentum Securities a.d., Novi Sad — https://momentum.rs/
3. Prudence Capital a.d., Beograd — https://prudencecapital.rs/

All screenshots are saved under `screenshots/<competitor>/`. Each competitor's folder contains: `01-home.png`, `02-services.png` (where available), `03-portfolio.png`, `04-education_news.png`, `05-contact.png`, `06-about.png`, `07-fees.png`. Raw extracted text is in `raw_data.json`.

---

## 1. Individual Competitor Summaries

### 1.1 Ilirika investments a.d., Beograd — `ilirika.rs`

**Screenshots:** `screenshots/ilirika/01-home.png` … `07-fees.png` (5 pages captured: home, portfolio, news, contact, legal/fees-fallback). Ilirika does not surface a dedicated unified "services" page — services are individual top-level pages.

**Hero / value proposition.** The site is anchored around a single navy-blue homepage tile grid. The most prominent on-page asset on capture day was a modal pop-up promoting **"Dan investitora" (Investor Day, 28 May)** at Hotel Marriott Courtyard, Belgrade — a live, in-person lead-generation event for asset management. The persistent headline message under the tiles is "Pomažemo vam da ostvarite ambicije za uvećanje vaših sredstava već više od 30 godina" ("Helping you grow your wealth for more than 30 years"). The four service tiles act as the real hero: *Berzansko posredovanje, Portfolio menadžment, Korporativni poslovi, ILIRIKA web trader*.

**Target audience.** Mixed but skewed toward **HNWI individuals and successful SMEs / corporates**. The portfolio management product is explicitly positioned with a **30,000 EUR minimum for individuals / 50,000 EUR for legal entities** — clearly affluent retail and corporate. M&A consulting is featured (corporate). Retail-trader audience is served through the *ILIRIKA web trader* tile but not deeply marketed.

**Visual style & branding.** Dark navy + steel-blue with white type, large hero photography (cityscapes, globes, mountains, industrial themes), serif/sans mix. Tone is **institutional, slightly heritage** — feels like a "private bank" aesthetic. Trust signals come from longevity ("30+ years"), the dual-jurisdiction footer (Belgrade + Ljubljana head office), and licensing references (Komisija za hartije od vrednosti). Visually a half-step behind modern web standards — some images feel stock-y and the layout is grid-rigid.

**Main CTAs & conversion strategy.** Primary CTAs are *WEB TRADER PRIJAVA* (top-right, for existing clients), *Zakažite sastanak* ("Book a meeting") on the portfolio management page, and a newsletter sign-up. Lead capture for portfolio management is a short three-field form (name, email, phone) — appropriately low-friction for a high-ticket service. There is **no online account-opening flow**.

**Overall positioning & credibility.** Positioned as a **regional, legacy, advisory-led** brokerage with Slovenian roots. Credibility is strong on paper (30+ year track record, dual office, licensed by the Serbian Securities Commission) but is **not visualized well**: no team page surfaced from the homepage, no client logos, no testimonials, no AUM number on the homepage. Credibility is *told*, not *shown*.

**Site structure & navigation.** Menu items (in nav order): Berzansko posredovanje · Portfolio menadžment · Korporativni poslovi · ILIRIKA web trader · Izdavanje obveznica · O ILIRICI · Novosti · Kontaktirajte nas. The site is service-flat — each service is a top-level page. Portfolio management is well explained on its own page (minimum ticket, why-us pillars, contact form, methodology bullets). Brokerage is more thinly described. **No structured onboarding for new investors** — no "How to start" walkthrough, no glossary, no calculator.

**Educational & content marketing.** Strongest content asset is a recurring **webinar series** ("Vebinar: Na razvijenom Zapadu (ništa) novo – disrupcija, rotacija, inflacija" — 22.04.2026; "Vebinar: Na Bliskom istoku (ništa) novo – mart kao test izdržljivosti finansijskog tržišta" — 16.03.2026; "Vebinar: Rezime ove i očekivanja za 2026. godinu na globalnom tržištu kapitala" — 15.12.2025). Plus the offline "Dan investitora" event. **No blog, no analyst reports surfaced publicly, no investor guides, no beginner-investor track**. Content is published as event announcements rather than evergreen learning.

**Lead generation & trust-building.**
- Newsletter sign-up: yes (footer).
- Contact form: yes, on portfolio-management page (3 fields).
- Live event (Dan investitora): yes, with Google Forms RSVP.
- Online account opening: **no** — only "contact us / book a meeting".
- License & regulator disclosure: yes, on the legal-info page (matični broj, PIB, licenca SEC, bank account); not on the homepage.
- Testimonials / client logos / case studies: **none surfaced**.
- Fees transparency: **none** — no tariff/fee schedule exposed.

**What they explicitly offer.**
- Online account opening: ✗
- Mobile app: ✗ (only ILIRIKA web trader, web-only)
- Client portal/trading platform: ✓ (ILIRIKA web trader)
- Investment calculator: ✗
- Portfolio performance examples: ✗
- Corporate investment services: ✓ (M&A advisory, bond issuance, corporate services)

| Strengths | Weaknesses |
|---|---|
| 30+ years longevity, regional (RS + SI) footprint | Outdated visual aesthetic vs. peers |
| Real M&A / corporate advisory depth | No fee transparency at all |
| Regular live webinars + flagship in-person event | No online onboarding; "call us" only |
| Clear minimum-ticket positioning for portfolio mgmt | No team page, no client proof, no AUM/numbers on homepage |
| Operates trading until 22:00 (implied via long hours) | Thin educational content for beginners |

- **Unique positioning:** Belgrade + Ljubljana dual presence; M&A / corporate finance pedigree.
- **Digital maturity:** Medium-low. Decent SEO meta description, some webinar cadence, but no funnel, no app, no fee page, no proof page.
- **Trust effectiveness:** Medium. Heritage cue is strong; institutional cues (licenses, two offices) are present but buried.
- **UX/UI:** Medium-low. Pop-up modal blocks the homepage on first visit; no sticky CTA; no investor-journey scaffolding.

---

### 1.2 Momentum Securities a.d., Novi Sad — `momentum.rs`

**Screenshots:** `screenshots/momentum/01-home.png` … `06-about.png` (5 pages captured: home, services, news/blog hub via homepage anchor, contact, about). No dedicated portfolio-mgmt landing page surfaced from the homepage navigation — portfolio management is one of six service blocks inside `/usluge/`.

**Hero / value proposition.** Rotating hero slider with four messages:
1. *"Kreirajte sami svoju budućnost"* ("Create your own future") → **POGLEDAJTE NAŠU BAZU ZNANJA** (View our knowledge base)
2. *"Pravi potez u pravo vreme"* ("The right move at the right time") → SAZNAJTE VIŠE O NAŠIM USLUGAMA
3. *"Trgujte pametno"* ("Trade smart") → SAZNAJTE VIŠE O NAMA
4. *"Nove prilike na dohvat ruke"* ("New opportunities at your fingertips") → SAZNAJTE VIŠE O E-CLIENT TRADER PLATFORMI

**Target audience.** Genuinely broad and explicitly stated on the services page: *"Nezavisno da li se radi o korporacijama ili individualnim klijentima, i da li ste iskusan investitor ili početnik"* ("Whether corporate or individual, experienced investor or beginner"). About page shows **>4,000 client contracts** and **>100 million EUR client assets under custody**. Client logo wall includes OTP Bank, Nectar, DDOR, Dunav DPF, Galenika Fitofarmacija, Mirotin Group, Novosadski sajam, IM Matijević, SEB, Danske Bank, FIMA Vrijednosnice, InterCapital — heavy on **mid-cap corporates and institutional counterparties**.

**Visual style & branding.** White + grey + a signature **red accent** (Pantone-bright red — used in logo, CTAs, the live-ticker arrows, blog illustrations). Modern flat-design aesthetic. Hero imagery: sailing ship's helm (steering = "navigation"); editorial photos of port/logistics, hands holding coins, charcoal-stock photography of finance. Tone is **modern, confident, navigation/journey metaphor**. This is the **most contemporary visual brand of the three**.

**Main CTAs & conversion strategy.** Primary: *Prijava* (login, top-right), *POGLEDAJTE NAŠU BAZU ZNANJA* (knowledge base), *PRIJAVI SE ZA NAŠ BILTEN* (newsletter, footer). No "Open account" CTA, no online onboarding. CTA hierarchy points readers to **content first** (Baza znanja, Vesti, Blog, Analize, Izveštaji), conversion second.

**Overall positioning & credibility.** "Iskusno. Predano. Transparentno." ("Experienced. Dedicated. Transparent.") Founded 2007, locally licensed brokers, full APR/PIB/LEI/BIC details on the about page, management ownership disclosure (646 shares = 55.7% of share capital — uncommon transparency). The client logo wall and AUM-style numbers on the about page are the **strongest credibility proof of any of the three**.

**Site structure & navigation.** Top nav: *USLUGE · VESTI I TRENDOVI (with sub-items: VESTI, BLOG, ANALIZE, IZVEŠTAJI) · E-CLIENT TRADER · O NAMA (O nama, Kako poslujemo, Naš tim, Karijera, Baza znanja) · KONTAKT*. The information architecture is **content-led** — Vesti i trendovi is the most prominent dropdown, with four distinct content types (news / blog / analyses / reports). Services are explained on a single `/usluge/` page with six numbered service blocks (Brokerske usluge, Upravljanje portfoliom, Usluge istraživanja i finansijske analize, Kastodi usluge, Korporativni agent i ostale investicione usluge, Korporativni finansijsko/pravni konsalting).

**Educational & content marketing.** **Best content depth of the three.** Four distinct streams advertised on the homepage:
- **Vesti** (news cards with imagery)
- **Momentum blog** (illustrated, "ideje bez ćoškova" style)
- **Analize** (analytical reports with thumbnails)
- **Izveštaji** (formal reports)
- **Kalendar događaja** (event calendar) — corporate-actions style
- **Baza znanja** (knowledge base) — beginner-investor educational resource referenced from the hero slider

A live cross-page ticker (S&P 500, Dow Jones, Russell 2000, AAPL, MSFT, GOOG, AMZN, NVDA, JPM, etc., via Twelve Data) reinforces "active, live, modern."

**Lead generation & trust-building.**
- Newsletter: yes (PRIJAVI SE ZA NAŠ BILTEN).
- Contact form: no obvious lead-capture form surfaced from homepage — contact page is informational (two offices).
- Online account opening: ✗.
- License / regulator: implied; about page lists APR registration BD 96764/2007, MB 20319780, PIB 105129854, LEI 747800V0X3N9TEEB9Y44, BIC MSNSRS21 — exemplary.
- Testimonials: no quoted testimonials, **but very strong client logo wall**.
- Fees transparency: **no public fee schedule** found.

**What they explicitly offer.**
- Online account opening: ✗
- Mobile app: ✗ (E-Client Trader appears to be web)
- Client portal/platform: ✓ (E-Client Trader)
- Investment calculator: ✗
- Portfolio performance examples: ✗
- Corporate investment services: ✓ (custody, corporate agent, financial-legal consulting)

| Strengths | Weaknesses |
|---|---|
| Strongest modern visual brand of the three | No online account opening |
| Deepest content engine (Vesti / Blog / Analize / Izveštaji / Baza znanja) | No fees published |
| Excellent corporate credibility wall (client logos + AUM + LEI/BIC) | No quoted testimonials |
| Live market ticker on homepage = "active broker" cue | No portfolio performance / track-record examples |
| Two offices (Novi Sad + Beograd) | Hero slider buries the value prop in four messages |

- **Unique positioning:** "Iskusno. Predano. Transparentno." with an editorial / publisher feel. Strongest content marketing in the market.
- **Digital maturity:** High. Content architecture, live data feeds, polished brand system.
- **Trust effectiveness:** High — best transparency on corporate identity & client list.
- **UX/UI:** High. Clean, modern, fast scan. Hero slider could be tightened.

---

### 1.3 Prudence Capital a.d., Beograd — `prudencecapital.rs`

**Screenshots:** `screenshots/prudence/01-home.png` … `07-fees.png` (full set of 7: home, services, portfolio, education/news = investment advisory, account opening, about, fees). Prudence is the only competitor that exposes every page in the target taxonomy.

**Hero / value proposition.** Quote hero — Jeremy Siegel ("Stocks for the Long Run") on a dark city-skyline background: *"Ulaganje u akcije je najsigurnije sklonište od inflacije"* ("Investing in stocks is the safest shelter from inflation"). Below the quote, three credibility logos: **Bloomberg · 25 godina iskustva · Interactive Brokers**. This is the **clearest single-sentence value prop of the three.**

**Target audience.** Both retail and corporate, but **digital-active retail investors are the obvious primary audience**: the homepage and onboarding flow promote *Interactive Brokers* and a *local web platform*, "ulaganje na preko 80 berzi širom sveta" (also says 150 elsewhere), and an explicit 3-step onboarding (Kontaktiraj → Otvori račun → Ispostavi nalog). Numbers on the homepage: **30,000+ klijenata · 300 mil. € imovina · 200 mil. € godišnji promet**. (Internal inconsistency: a secondary "Prudence u brojkama" block lower on the homepage shows 27,320+ / 264 mil. € / 169 mil. € — they didn't normalize the two numeric blocks.)

**Visual style & branding.** Navy-blue + **red accent** + white. Custom "Prudence" U-mark logo. Dark hero with city imagery, large white serif quote, clean tile grids. Tone is **confident, modern-classic** — somewhere between a private wealth manager and a fintech. Sub-pages reuse the same modular components (hero strip → intro paragraph → red divider → numbered/iconified value pillars). Visual coherence across pages is strong.

**Main CTAs & conversion strategy.** Primary: *Otvori račun* in main nav (the only competitor with a "Open account" link in primary nav), *Kontaktirajte sa nama* footer-block, *LinkedIn* badge in footer. The **3-step graphical onboarding** ("Započnite investiranje na berzi u 3 koraka") on the homepage is a textbook conversion device. The `/otvori-racun/` page has **two parallel onboarding tracks** (local WEB platform vs. Interactive Brokers), each presented as 4-step processes — best-in-class onboarding clarity in this set.

**Overall positioning & credibility.** "Sa preko 25 godina iskustva … jedan od vodećih brokersko-dilerskih društava u Srbiji." Heritage story: founded **1996 as Delta Broker**, rebranded to Prudence Capital after a 2012 ownership change (founder Nebojša Divljan). Bloomberg + Interactive Brokers + 25-year heritage = a tight, repeatable trust triangle. Full named team (Nebojša Divljan / Founder, Darko Dostanić / GM, Irena Babić / Exec Director, Saša Odalović, Ilija Protić CFA, Stefan Majkić, Filip Žemlje) on the About page — **the only competitor that names licensed brokers individually**, and the only one to surface a **CFA charterholder** as CIO.

**Site structure & navigation.** Top nav: *O nama (O kompaniji, Naš tim, Autorski tekst osnivača, Opšti podaci i akta) · Usluge (Brokerski poslovi, Investiciono savetovanje, Portfolio menadžment, Korporativne usluge) · Tarifnik (IBKR platforma, Lokalna WEB platforma) · Otvori račun · Blog (Vesti sa tržišta, Vodič za investitore, Obaveštenja) · Kontakt*. This is the **most complete and logically structured IA** of the three.

**Portfolio management is best-in-class.** Five named portfolio types with explicit asset allocations:
- **Visok prinos** — 98% akcije / 2% novac
- **Balansirani** — 60% akcije / 33% obveznice / 5% alternativna / 2% novac
- **Nizak rizik** — 75% obveznice / 15% akcije / 5% alternativna / 5% novac
- **Indeksirani dugoročni SIP** — pasivni dugoročni plan, mali inicijalni ulog
- **Specijalizovani** — bespoke

A documented "top-down" methodology (macro → sector → company) with a satellite theme overlay (green tech, cybersecurity, AI). A four-step engagement process. A disclaimer about past performance. **No other Serbian brokerage on this list explains its portfolio offering at this level of structure.**

**Educational & content marketing.**
- *Blog* sub-menu with three streams: **Vesti sa tržišta**, **Vodič za investitore** (literally "Investor's Guide" — closest thing to a beginner education track in this set), **Obaveštenja** (notices).
- Founder's "Autorski tekst" (a personal essay from the founder framing the inflation/savings argument) — strong thought-leadership lever, rare in this market.

**Lead generation & trust-building.**
- Newsletter: not surfaced on homepage (potential gap).
- Contact form: standard contact details on each page, contact page accessible.
- **Online account opening: clear documented process, two tracks** (local WEB platform + IBKR). Still requires offline signing of the brokerage contract — true e-onboarding is not present.
- License & regulator: yes, in *Opšti podaci i akta*.
- Testimonials: none surfaced.
- **Fees transparency: yes — full Tarifnik page.** Progressive vs. Basic tier (PROGRESIV: SAD 0.15% / EU 0.20%; BASIC: SAD 0.3% / EU 0.35%), minimum order fees in USD/EUR, options/futures at $3/€3 per contract, custody at 0.2% p.a., transfer fees 25 EUR per ISIN. **Only competitor that publishes prices.**

**What they explicitly offer.**
- Online account opening: ✓ (documented, hybrid process)
- Mobile app: ✗ (no mobile app referenced; IBKR mobile is the implicit answer)
- Client portal/platform: ✓ (Local WEB platform + IBKR)
- Investment calculator: ✗
- Portfolio performance examples: portfolio *types* are documented; historical returns not published (just a "past performance" disclaimer)
- Corporate investment services: ✓ (Korporativna agentura, Finansijsko-pravni konsalting)

| Strengths | Weaknesses |
|---|---|
| Tightest value prop and IA of the three | Numeric inconsistency on homepage (27.3k vs 30k clients) |
| Only one with published fees (Tarifnik) | No published historical portfolio performance |
| Best-structured portfolio management offering | No newsletter sign-up surfaced on homepage |
| Named team with credentials (CFA charterholder visible) | No client testimonials or logo wall |
| Best onboarding flow (3-step + 4-step) and "Otvori račun" in nav | No mobile app of their own |
| Founder thought-leadership essay | Lower content velocity than Momentum |

- **Unique positioning:** *Prudence* = "promišljeno, oprezno i mudro investiranje" + IBKR partnership + 25-year heritage as Delta Broker → Prudence Capital.
- **Digital maturity:** High. Best conversion architecture in the set.
- **Trust effectiveness:** High. Named team + CFA + IBKR + Bloomberg + fee transparency = best trust stack.
- **UX/UI:** High. Cleaner than Ilirika, more conversion-focused than Momentum.

---

## 2. Cross-Competitor Comparison

### 2.1 Quick comparison matrix

| Dimension | Ilirika | Momentum | Prudence |
|---|---|---|---|
| Heritage claim | 30+ years | Since 2007 | 25+ years (since 1996 as Delta Broker) |
| Visual modernity | Medium-low | **High** | High |
| Single clearest value prop | No (modal-driven) | No (4-rotation slider) | **Yes** (Siegel quote + 3-logo trust bar) |
| Live market data on homepage | ✗ | **✓** | ✗ |
| Listed services page | Implied via tiles | ✓ | ✓ |
| Portfolio mgmt explained with risk tiers | Generic | Generic | **✓ (5 named portfolios)** |
| Online account opening flow | ✗ | ✗ | **✓** (documented, hybrid) |
| "Open account" CTA in main nav | ✗ | ✗ | **✓** |
| Fees published | ✗ | ✗ | **✓** (Tarifnik) |
| Named team / individual brokers | ✗ | ✓ (link "Naš tim") | **✓ (with photos + CFA charter)** |
| Client logo wall | ✗ | **✓** | ✗ |
| AUM / client numbers on homepage | ✗ | About page only | **✓ (30k+/300M€/200M€)** |
| Testimonials / quoted clients | ✗ | ✗ | ✗ |
| Blog | ✗ (only event news) | **✓ (Blog + Analize + Izveštaji)** | ✓ (Vesti + Vodič + Obaveštenja) |
| Beginner-investor track | ✗ | Baza znanja (referenced) | **Vodič za investitore** |
| Regular webinars | **✓ (multi-year cadence)** | ✗ | ✗ |
| In-person investor events | **✓ (Dan investitora)** | Kalendar događaja | ✗ |
| Mobile app | ✗ | ✗ | ✗ |
| Investment calculator | ✗ | ✗ | ✗ |
| Newsletter sign-up | ✓ (footer) | ✓ (footer) | ✗ (not surfaced) |
| Social media surfaced | ✗ | ✓ (footer icons) | ✓ (LinkedIn footer) |
| IBKR / Bloomberg partnership badges | ✗ | ✗ | **✓** |
| Multi-language site (EN) | ✗ | **✓** | ✗ |
| HNWI explicit minimum | **✓ (30k €/50k €)** | ✗ | ✗ |

### 2.2 Common patterns across Serbian brokerage firms

1. **"Tell, don't show" trust building.** Each emphasizes years of experience, licensing, and a leadership/regulator disclosure — but **none surface client testimonials**, and only Momentum surfaces client logos. No video case studies, no investor stories, no LinkedIn-style social proof. The category sells trust verbally.
2. **No real online account opening anywhere.** Even Prudence — the most documented — still requires a paper signature with a correspondent bank. Account opening is universally a 3-to-4-step "call us, sign with us, fund through a bank, start trading" hybrid. This is partly regulatory (KYC/AML in Serbia is paper-anchored), but it is also an unexploited differentiation lever.
3. **Mobile is a blind spot.** **No competitor markets a native mobile app of their own.** IBKR mobile is the implicit answer for Prudence; the other two are web-only.
4. **Fees are not a competitive instrument.** Only Prudence publishes a tariff. The other two require a phone call to find out what trading costs.
5. **Content is the strongest differentiator already in play.** Momentum has invested most heavily here (Vesti, Blog, Analize, Izveštaji, Baza znanja). Prudence has a thinner but well-structured blog (notably "Vodič za investitore"). Ilirika treats content as event announcements only.
6. **Heritage is the dominant trust device.** Every brand leads with years on the market (30+ / since 2007 / 25+). This makes longevity table stakes, not differentiation.
7. **Belgrade-centric, with one regional outlier.** Two of three are Belgrade-only; Momentum has Novi Sad + Belgrade. None has a visible third-city presence.
8. **Visual templates are converging.** All three rely on dark-blue or navy hero + red/orange accent + city/finance stock photography + numbered tiles. The category looks generic from 10 ft.
9. **English-language presence is sparse.** Only Momentum has an EN switch surfaced. This caps cross-border / diaspora / Western-domiciled-Serbian capital reach.
10. **Educational content for beginners is the largest unmet need.** Only Momentum's "Baza znanja" (referenced) and Prudence's "Vodič za investitore" point at this market. Neither runs a serious beginner curriculum.

### 2.3 Gaps in the market

| Gap | Where it shows up | Why it matters |
|---|---|---|
| No serious beginner curriculum (videos, glossary, "what is an ETF", risk tolerance quiz) | All three | Retail growth in Serbia depends on first-time investors |
| No published portfolio performance / track-record | All three | First question every retail investor asks |
| No native mobile app | All three | Younger investors expect mobile-first |
| No investment calculators (compound interest, FX, fee calculator) | All three | Calculators are organic-traffic magnets |
| No client testimonials or quoted stories | All three | Strongest possible social proof in a low-trust category |
| Fee transparency only present at one of three | Ilirika, Momentum | Implicit signal of opacity to a price-sensitive market |
| English-language site | Ilirika, Prudence | Diaspora capital, foreign HNWIs in Belgrade |
| Tax / regulatory plain-language guidance | All three | Tax on capital gains is the #1 retail investor confusion |
| Dedicated HNWI / family-office segmentation | Only Ilirika (via 30k € min.) | Premium positioning lever |
| Corporate / SME treasury proposition page | Partly present | Cash-rich Serbian SMEs are an underserved segment |

### 2.4 Opportunities Tesla Capital could exploit

- **Be the brokerage that publishes performance.** A live (delayed/aggregate) representative-portfolio dashboard would be a category-first.
- **Be the brokerage that opens an account online.** Even a partial digital-onboarding flow (KYC upload, video ID, signed e-doc, mailed wet-signature only at the end) would beat every competitor's current state.
- **Be the brokerage with the best beginner academy.** Free, branded, structured curriculum (10-15 short video lessons + glossary + quizzes) — this is a content moat, not a one-off campaign.
- **Be the brokerage with the calculator suite.** Compound-interest, EUR/RSD inflation comparison vs. bank deposit, ETF cost calculator, capital-gains tax estimator — each is one organic-search page that can carry the funnel.
- **Be the brokerage with a real mobile app.** Even a read-only client portal app would beat the current field.
- **Be the brokerage that segments visibly.** Three doors on the homepage: *Početnik* (Beginner), *Aktivan investitor* (Active investor), *Korporacija / HNWI*.
- **Be the brokerage with a public Tarifnik that wins on comparison.** Match-or-beat Prudence's published rates and put a comparison table on the page.

### 2.5 Strongest online presence in the set

**Prudence Capital** has the strongest overall online presence. Reasons:

1. **Clearest value proposition** (the Siegel quote + 3-logo trust bar = inflation hedge + Bloomberg + IBKR + 25 years).
2. **Strongest conversion architecture**: "Otvori račun" in the primary nav; documented 3-step homepage flow; full account-opening sub-page with two parallel platform tracks.
3. **Most transparent**: only one with a public Tarifnik, named team including CFA charterholder, full corporate disclosure.
4. **Best portfolio management explanation** in the market — five named portfolios with explicit asset allocations.
5. **Most coherent IA**: nav is the cleanest, sub-menu structure is logical, every key target page exists.

**Momentum** is a strong second, with the **best content engine and most modern visual brand** but a weaker conversion path (no account-opening CTA in nav, no published fees). Ilirika is a clear third — strong on heritage and offline events, weakest on digital fundamentals.

---

## 3. Strategic Recommendations for Tesla Capital

### 3.1 How Tesla Capital can stand out online

Tesla Capital should commit to one defensible position: **"The most transparent and accessible brokerage in Serbia."** It is the empty quadrant of this competitive map: transparency (Prudence partial, others none) + accessibility (no one has it). Positioning lines to test:

- *"25 godina iskustva, transparentne provizije, prvi račun u 24 sata."* — "25 years of experience, transparent fees, first account in 24 hours."
- *"Berza za sve — od prvog dinara do prvog miliona."* — "The market for everyone — from your first dinar to your first million."

Reinforce with three permanent on-site assets that none of the three competitors has:

1. A **published Tarifnik** with a side-by-side comparison vs. domestic bank deposits and ETFs.
2. A **performance dashboard** showing a representative model portfolio (with appropriate disclaimer).
3. A **client testimonial wall** — even 6 named retail clients with photo + 2-sentence quote will out-trust every competitor.

### 3.2 Services / features to emphasize

- **Online (or guided-digital) account opening.** Document the steps publicly. Promise a target time (e.g. "račun za 48 sati"). Put "Otvori račun" in the primary nav.
- **Three explicit client segments on the homepage.** Beginner / Active trader / Corporate–HNWI. Each segment routes to its own landing page with its own CTA.
- **Portfolio management with named portfolios and risk tiers**, modeled on Prudence's structure — but go one step further by publishing **rolling 3y / 5y representative returns**, with disclaimers.
- **Corporate treasury / SME investment** as a distinct service line, not a sub-bullet. Serbian SMEs sit on cash and have nowhere to deploy it short of bank deposits.
- **Live market data ticker** on the homepage (like Momentum's) — cheap to license (TwelveData, Finnhub), high credibility per pixel.
- **A mobile app or a polished mobile-web client portal** as the next differentiator after the previous ones are live.

### 3.3 Educational content that will attract retail investors

Tesla Capital should build a single, named, branded academy — e.g. **"Tesla Akademija"** or **"Vodič za investitore"** — with the following content backbone:

- **15 short video lessons** (3-6 min each) covering: *Šta je akcija? · Šta je ETF? · Kako se računa prinos? · Šta su dividende? · Šta je rizik i kako ga meriti? · Kako čitati godišnji izveštaj kompanije? · Domaće vs. strane berze za srpskog investitora · Porez na kapitalnu dobit u Srbiji · Inflacija i čuvanje kupovne moći · Dollar-cost averaging · Diversifikacija · Greške početnika · Top-down vs. bottom-up · Kako razumeti Tarifnik · Otvaranje računa korak po korak.*
- **Glossary** (50-100 terms, Serbian + English) — built once, ranks forever for definitional queries.
- **3 quizzes**: risk tolerance, knowledge level, "koji portfolio je za vas?" — all act as soft lead-capture.
- **A monthly "Investitor mesec" newsletter** (anchor format: 1 market take + 1 mini lesson + 1 client question + 1 chart). Mirror Momentum's frequency cadence but with a teaching voice.
- **"Vodič za prvih 1.000 EUR"** and **"Vodič za prvih 100.000 EUR"** — two long-form pillar pages segmented by ticket size. Both will rank.
- **Tax explainers**, refreshed every January when Serbian tax forms come due.

### 3.4 Attracting corporate / HNWI clients

- **A separate "Tesla Capital Private" or "Tesla Capital Corporate" landing track** — distinct hero, distinct CTAs (Zakažite sastanak), distinct numbers (minimum ticket, named relationship managers).
- **Named senior bankers with photos, CFAs/MBAs surfaced** (mirror Prudence's CIO surfacing — but with full team).
- **LinkedIn thought leadership** from named bankers (founder's column, head of research bi-weekly note).
- **In-person events** (mirroring Ilirika's "Dan investitora") for the top of the HNWI funnel; quarterly Belgrade + Novi Sad + Niš rotation.
- **A confidential "case study" deck** — anonymized, with sectors and outcome numbers — handed to qualified leads.
- **English-language version of the site and key collateral** to capture diaspora and Western HNWIs domiciled in Belgrade.

### 3.5 Website UX improvements

- Replace any homepage cookie pop-up or modal pop-up at first paint. (Ilirika lost the first paint to a modal on capture day.)
- **Single message hero** instead of 4-slide carousels (Momentum lesson).
- **Sticky primary CTA** ("Otvori račun" / "Zakaži sastanak") on every page.
- **Three-door segmentation** below the hero (Beginner / Active / Corporate–HNWI).
- **Trust bar** below the hero with three artifacts: regulator (Komisija za hartije od vrednosti), 25-year heritage badge, headline number (AUM or clients) — Prudence-style.
- **Hard numbers** on the homepage: clients, AUM, year founded. Keep one canonical number — never have two conflicting numbers on the same page (Prudence's 27.3k vs 30k is a lesson).
- **Performance + tariff visible from primary nav** — both are "first 30 seconds" questions.
- **Fast, mobile-first build**, target Core Web Vitals all-green; the category is slow.
- **English language toggle** in the header.

### 3.6 Trust-building recommendations

- **Publish the Tarifnik publicly** (match-or-beat Prudence on simplicity).
- **Publish a representative portfolio's monthly NAV** (with disclaimers + factsheet).
- **Show the team**: photos, names, credentials (CFA, FRM, MBA, where applicable).
- **Show the regulator**: footer badge with Komisija za hartije od vrednosti registration number + link to the public license register.
- **Client testimonials**: 6-8 named retail clients (photo, role, sector, 2-sentence quote) + a corporate logo wall (mirroring Momentum's, but with permission slips collected).
- **Annual "Letter to investors" / market outlook** PDF, branded — a thought-leadership artifact that travels.
- **Compliance / risk-disclosure links** in the footer; transparent, not buried.
- **Independent press mentions** (e.g. Bloomberg Adria, Forbes Srbija, Bizlife, Politika) collected on a "U medijima" page.

### 3.7 Suggested lead generation funnels

| Stage | Channel | Asset | KPI |
|---|---|---|---|
| Awareness (Beginner) | SEO / YouTube | "Vodič za prvih 1.000 EUR" pillar + 15 video lessons | Organic sessions, video watch-through |
| Awareness (Corporate) | LinkedIn + PR | Founder column + quarterly market outlook PDF | LinkedIn followers, PDF downloads |
| Interest | Site | Risk-tolerance quiz / "Koji portfolio je za vas?" | Quiz starts → completes |
| Consideration | Email | Monthly "Investitor mesec" newsletter | Open rate, click rate |
| Consideration (HNWI) | Events | Quarterly "Dan investitora" Belgrade/Novi Sad | RSVPs, attended, MQLs |
| Intent | Site | Calculators (inflation, fees, capital-gains tax) | Calculator → contact form |
| Intent | Site | "Otvori račun" wizard (multi-step form, save & resume) | Account-open starts → completes |
| Decision | Direct | Booked discovery call with portfolio manager | Calls booked → contracts signed |
| Retention | App / portal | Mobile portal, push alerts, weekly digest | DAU/MAU, retention curve |

Two specific funnels worth standing up first:

- **"Prvi račun u 48 sati"** — landing page → KYC checklist → upload documents → calendar booking with a broker → confirmation. End-to-end measurable, immediately differentiating.
- **"Investitor mesec"** — bottom-of-page newsletter form + popup at 60% scroll + content-gate on the longer pillar pages. Compounds into the largest owned distribution channel in the category.

### 3.8 Modernizing brand perception

- **Rebuild the visual system** around a single coherent palette (consider keeping Tesla's current accent color but flatten the secondary palette to two neutrals).
- **Custom illustration system** instead of stock finance photography — none of the three competitors has owned illustration, and it is the single fastest way to look different.
- **Original photography** of the actual Belgrade office, the actual brokers, the actual trading floor — mirrors Prudence's strongest tactic.
- **Type system upgrade** — pick one editorial-grade Serbian-Cyrillic-and-Latin sans (e.g. Inter, IBM Plex, Söhne) and use it consistently.
- **Motion / micro-interactions** on hover and on scroll — modest, but absent in all three competitors.
- **Accessibility / dark mode** — both invisible in the category; both signal that the brand cares.

---

## 4. Marketing Recommendations

### 4.1 Social media & content opportunities

- **LinkedIn first.** All three competitors are weak here (only LinkedIn icons in footers, no editorial cadence visible). 2-3 posts/week from named bankers (founder, CIO, head of research) is enough to dominate share-of-voice in the Serbian finance LinkedIn graph within 6 months.
- **YouTube as the academy host.** The "Tesla Akademija" videos live on YouTube and embed on the site. Each video is also a 60-second short. Each video has a SEO-optimized title in Serbian.
- **Instagram + TikTok** for retail / younger investors. Format: 30-60 sec explainers, weekly. Topic backlog: *Šta je akcija? · Šta je dividenda? · Kako se računa P/E? · Inflacija vs. depozit · Dollar-cost averaging u Srbiji.*
- **Webinar program** (steal/extend Ilirika's webinar cadence) — monthly, named, recorded, gated. Build a webinar series brand (e.g. *Tesla Insight*).
- **Beograd / Novi Sad investor meetups** — quarterly, in-person, with one outside speaker (academic, journalist, fund manager).

### 4.2 SEO & content strategy ideas

- **Pillar pages** — long, definitive guides built once, refreshed quarterly:
  - *Kako kupiti akcije u Srbiji 2026*
  - *Najbolji ETF-ovi za srpske investitore*
  - *Porez na kapitalnu dobit u Srbiji – kompletan vodič*
  - *Beogradska berza vs. svetske berze – gde investirati*
  - *Razlika između štednje i investiranja*
  - *Otvaranje brokerskog računa korak po korak*
  - *Šta je portfolio menadžment – sve što treba da znate*
- **Calculator pages** (rank for high-intent queries):
  - Kalkulator složene kamate
  - Kalkulator inflacije u Srbiji
  - Kalkulator prinosa investicija
  - Kalkulator poreza na kapitalnu dobit
  - Kalkulator brokerskih provizija
- **Comparison pages** (high-intent commercial queries): *Tesla Capital vs. [konkurent]*, *Tesla Capital Tarifnik vs. domaće banke depoziti*, *Tesla Capital vs. IBKR direktno*.
- **Local SEO** — register and fully populate Google Business Profile for Belgrade office; add reviews flow; localize the Beogradski / Novosadski address pages.
- **Internal linking** — every blog article links to a relevant calculator + a relevant pillar page + the "Otvori račun" CTA.

### 4.3 Thought leadership topics

For founder / CIO / Head of Research bylines:

- *Inflacija i čuvanje kupovne moći u dinarima — gde su pravi otklonski instrumenti?*
- *Zašto srpski investitori treba da gledaju iznad Beogradske berze*
- *AI, sajber bezbednost, zelene tehnologije — tematska ulaganja za 2026.*
- *Kako analizirati godišnji izveštaj kompanije u 30 minuta*
- *Šta zaista znače Buffettovi „margins of safety" za srpskog investitora*
- *Privatni penzioni fondovi vs. samostalno investiranje — uporedna analiza za Srbiju*
- *Korporativna gotovina: kako srpske kompanije mogu da je razmeste pametnije od depozita*

### 4.4 Investor education initiatives

- **Tesla Akademija** — the 15-lesson backbone above, all free, all gated only by email.
- **"Prvi račun" workshop** — monthly, online, 45 min, branded, with a recorded library.
- **University talks** — Ekonomski fakultet (Beograd), Ekonomski fakultet Subotica, FON, BBA — 2 per semester. Recruit + brand awareness in one motion.
- **Annual investor outlook** PDF — distributed every January, branded, picked up by financial press.
- **Quarterly "Pitajte Tesla" Q&A livestream** — answer reader-submitted questions, recorded for evergreen YouTube.

### 4.5 Conversion optimization ideas

- **Always-visible top-bar CTA**: "Otvori račun za 48h" (test exact copy).
- **3-step homepage onboarding visual** (mirror Prudence's "Započnite investiranje u 3 koraka" — borrow the format, beat it on copy).
- **Exit-intent popup** offering the "Vodič za prvih 1.000 EUR" PDF in exchange for an email.
- **Save-and-resume account-opening wizard** (sign-up by email, resume later by link). Tested KYC-flow tactic; nobody in the Serbian market has it.
- **A/B test the hero**: quote-led (Prudence model) vs. promise-led (e.g. "Račun u 48 sati") vs. proof-led (e.g. "30,000+ srpskih investitora veruje nama"). Pick a winner before scaling traffic.
- **Trust bar above the fold** with three artifacts: regulator badge, IBKR/Bloomberg or equivalent partnership, anchor number (clients / AUM / years).
- **Calculator → contact form** pattern: every calculator ends with "Razgovarajte sa investicionim savetnikom".
- **Reviews & ratings** — even an internal "verifikovani klijent" rating widget (with a simple post-onboarding NPS form) outperforms the current zero in the category.
- **Lead scoring + Meet-with-a-broker calendar** (Calendly or equivalent embedded) for HNWI-flagged form submissions.

---

## 5. Deliverables

All assets are on disk under `/Users/ogurianova/Desktop/TESLA/competitive-analysis/`:

| Asset | Path |
|---|---|
| This report | `REPORT.md` |
| Capture script (re-runnable) | `capture.py` |
| Raw extracted text per page | `raw_data.json` |
| Ilirika screenshots | `screenshots/ilirika/01-home.png` … `07-fees.png` (5 files) |
| Momentum screenshots | `screenshots/momentum/01-home.png` … `06-about.png` (5 files) |
| Prudence screenshots | `screenshots/prudence/01-home.png` … `07-fees.png` (7 files) |

### 5.1 Suggested first 90-day roadmap for Tesla Capital

| Days | Workstream | Deliverable |
|---|---|---|
| 0–30 | Foundation | Publish **Tarifnik** page · publish **named team page** with photos + credentials · add **regulator badge** and headline numbers to homepage · add **English toggle** stub |
| 0–30 | Funnel | Stand up **"Otvori račun"** primary-nav CTA + 4-step page (mirroring Prudence) with target SLA "48 sati" |
| 30–60 | Content engine | Launch **Tesla Akademija** (3 videos + glossary + 1 quiz) · launch **monthly newsletter** ("Investitor mesec") · stand up **3 calculators** (compound interest, inflation, capital-gains tax) |
| 30–60 | Brand refresh | New homepage hero (single quote-led message + 3-logo trust bar) · custom illustration system kickoff · removal of stock finance imagery from top of funnel |
| 60–90 | Authority | Publish **2 pillar pages** ("Kako kupiti akcije u Srbiji 2026", "Porez na kapitalnu dobit – kompletan vodič") · founder LinkedIn cadence live (2 posts/week) · first quarterly **Tesla Insight webinar** booked |
| 60–90 | HNWI track | Launch **Tesla Capital Private** sub-brand landing page · first in-person **Dan investitora**-style event scheduled · case-study deck (anonymized) for sales team |

This sequence puts Tesla Capital ahead of all three competitors on **transparency** (Tarifnik + numbers + named team) inside 30 days, ahead on **conversion funnel** at day 60, and ahead on **owned audience** (newsletter + LinkedIn) by day 90 — without requiring native app development, which can be planned in the next quarter once these baseline gaps are closed.
