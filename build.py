"""Generate 3 TurnKey landing pages from shared template + per-page data.

Phase A rebuild (Jun 26 PM): single-column body copy, per-page section order from
Dimi's spec, one mp4 per page mid-page, testimonials moved up to right after the
above-fold body, unified "Get my free quote" CTA, no cards/numbered indexes.

Phase C: real draggable before/after split-slider (vanilla JS, 2 pairs per page).
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

LOGO = "https://www.turnkeybathremodel.com/wp-content/uploads/2023/12/logo.png"
PHONE_DISPLAY = "(504) 784-1784"
PHONE_HREF = "tel:+15047841784"
CTA_LABEL = "Get my free quote"

# Shared assets
TESTIMONIALS = [
    ("Beautiful work and finished a day early. The crew was clean, on-time, and the fixed price never changed. Highly recommend.", "Robert White", "New Orleans, LA · Google Review"),
    ("We had a tub-to-shower conversion done in 2 days. The team was professional and the acrylic walls look amazing. No grout to scrub.", "Linda M.", "Metairie, LA · Google Review"),
    ("They walked us through everything at the consultation. No pressure, fixed quote, and the install was finished when they said it would be.", "James K.", "Mandeville, LA · Google Review"),
    ("My elderly mother needed a walk-in tub. TurnKey was patient, careful with her home, and the install was perfect. She finally feels safe bathing.", "Cheryl T.", "Lakeview, LA · Google Review"),
    ("Best bathroom remodel decision we made was going with a local team. No subcontractors, one crew, done in 3 days.", "Marcus B.", "Garden District, LA · Google Review"),
    ("Got 3 quotes and TurnKey was the only one who gave us a real fixed price up front. No surprises, work was top quality.", "Sarah P.", "Uptown, LA · Google Review"),
]

# ============ PAGE DATA ============
PAGES = {
    "bathroom-remodeling-contractor": {
        "slug": "bathroom-remodeling-contractor",
        "title_tag": "New Orleans Bathroom Remodeling Contractor | TurnKey Bath",
        "meta_desc": "Licensed New Orleans bathroom remodeling contractor. Fixed-price quotes, most projects done in 1 to 3 days, free $250 design consult. Call (504) 784-1784.",
        "h1": "New Orleans Bathroom Remodeling Contractor",
        "hero_img": "images-finished-bath/IMG_3187.jpg",
        "hero_img_alt": "Finished bathroom remodel by TurnKey Bath Remodel — New Orleans",
        "badge": "Bathroom Remodeling · Greater New Orleans",
        "subhead": "A licensed, locally owned bathroom remodeling team serving Greater New Orleans. Fixed-price quotes, most projects finished in 1 to 3 days, and a free in-home design consultation worth $250.",
        "above_fold_body": "Looking for a bathroom remodeling contractor in New Orleans who shows up, quotes a fixed price, and finishes on time? TurnKey Bath Remodel is a locally owned company that does one thing: bathrooms. We have remodeled bathrooms across the Greater New Orleans metro for more than 25 years, and we hold a 4.9 Google rating from hundreds of five-star reviews. From your free design consultation through final cleanup, you work with one dedicated team. No subcontractors, no hand-offs, no surprise costs.",
        "video_src": "page1-video.mp4",
        "video_heading": "See a TurnKey bathroom remodel come together",
        "video_caption": "AI montage of finished bathroom remodels by our New Orleans team.",
        "form_dropdown_options": ["Full bathroom remodel", "Shower", "Tub-to-shower conversion", "Walk-in tub", "Not sure yet"],
        # Per-page body sections — order matches DEV-HANDOFF lines 167-186
        "sections": [
            ("What we remodel", "We remodel bathrooms and only bathrooms: full bathroom remodels, shower installations, shower replacements, tub-to-shower conversions, bathtub replacements, walk-in tubs, and barrier-free showers. Because bathrooms are all we do, you get a team that knows waterproofing, ventilation, and fixture work, not a general contractor who treats your bathroom as a side job."),
            ("Why New Orleans homeowners choose a specialist", "We are locally owned and have worked in homes from Lakeview to the Garden District, Metairie to Mandeville. We understand what older New Orleans homes and our humidity do to a bathroom, and we build with premium, American-made materials chosen to hold up in this climate. Every job is backed by a lifetime guarantee on acrylic products and a 10-year workmanship guarantee."),
            ("Fixed-price quotes, no surprises", "Many contractors give a vague estimate and let the number creep. We do not. You get a fixed-price guaranteed quote before any work starts, so you know exactly what your remodel will cost. No change orders, no hidden fees, no bait-and-switch."),
            ("Done in days, not weeks", "Most of our projects are completed in 1 to 3 days, and many in as little as a single day. You keep your home and your routine instead of living around a job site for weeks."),
            # video block inserts here (after index 3)
            ("Licensed, insured, and local", "TurnKey Bath Remodel is fully licensed and insured: Residential License #890459 and Commercial License #3667. We are lifelong members of this community, we answer our own phone, and we treat every project as if it were in our own home. That is part of how we earned a 4.9 Google rating and hundreds of five-star reviews from New Orleans neighbors."),
            ("0% financing", "A new bathroom should fit your budget, not strain it. We offer 0% financing so you can move forward with flexible monthly payments."),
            ("Service area", "We serve Greater New Orleans and the surrounding metro, including Lakeview, Garden District, Uptown, Metairie, Mandeville, and the Northshore."),
        ],
        "video_after_index": 3,  # insert video block after "Done in days, not weeks"
        "faqs": [
            ("How much does a bathroom remodel cost in New Orleans?", "It depends on the size of the room, the materials you choose, and what your home needs behind the walls. Rather than guess, we give you a fixed-price guaranteed quote at your free consultation, and we offer 0% financing."),
            ("How long does a bathroom remodel take?", "Most of our projects are finished in 1 to 3 days, with many done in a single day."),
            ("Are you licensed and insured?", "Yes. We are fully licensed and insured: Residential License #890459 and Commercial License #3667."),
            ("What if you find a problem behind the wall?", "We give you a fixed-price guaranteed quote up front and stand behind it. You will not be hit with surprise change orders."),
            ("Do you offer financing?", "Yes, 0% financing is available."),
        ],
        "closing": "Ready for a bathroom that is built right and priced honestly? Book your free in-home design consultation, a $250 value, or call our team now.",
        "ba_pairs": [
            ("images-ba/p1-ba1-before.jpg", "images-ba/p1-ba1-after.jpg", "Full bathroom remodel"),
            ("images-ba/p1-ba2-before.jpg", "images-ba/p1-ba2-after.jpg", "Vanity & tile refresh"),
        ],
    },
    "bathtub-and-shower-remodeling-contractor": {
        "slug": "bathtub-and-shower-remodeling-contractor",
        "title_tag": "Bathtub and Shower Remodeling Contractor | New Orleans",
        "meta_desc": "Walk-in showers, shower replacements, and tub-to-shower conversions in New Orleans. Fixed-price quotes, most installs 1 to 3 days. Call (504) 784-1784.",
        "h1": "Bathtub and Shower Remodeling Contractor",
        "hero_img": "images-finished-bath/PHOTO-2023-11-14-12-50-53_a.jpg",
        "hero_img_alt": "New walk-in shower install by TurnKey Bath Remodel — New Orleans",
        "badge": "Showers & Tub Conversions · New Orleans",
        "subhead": "New Orleans walk-in showers, shower replacements, and tub-to-shower conversions. Fixed-price quotes, most installs finished in 1 to 3 days, and a free design consultation worth $250.",
        "above_fold_body": "Ready to replace a worn-out shower or convert an old tub into a walk-in shower? TurnKey Bath Remodel installs walk-in showers, shower replacements, and tub-to-shower conversions across New Orleans. We are a locally owned company that does only bathrooms, with a 4.9 Google rating and hundreds of five-star reviews. Our acrylic shower systems have no grout lines to scrub or reseal, which matters in New Orleans humidity. You get a fixed-price quote before we begin, and most installs are finished in 1 to 3 days.",
        "video_src": "page2-video.mp4",
        "video_heading": "Walk-in shower installs done in 1 to 3 days",
        "video_caption": "AI montage of recent walk-in shower and tub-to-shower conversion installs.",
        "form_dropdown_options": ["Walk-in shower", "Shower replacement", "Tub-to-shower conversion", "Barrier-free shower", "Not sure yet"],
        "sections": [
            ("Showers we install", "Walk-in showers with easy entry and a clean, open look. Shower replacements that swap a dated or leaking shower for a new system. Tub-to-shower conversions that turn an unused tub into a full walk-in shower. Barrier-free and curbless showers for safer, step-free entry. Walk-in showers with a built-in seat or bench."),
            ("Tub-to-shower conversions", "A tub-to-shower conversion is one of the most-requested bathroom projects in New Orleans, and it is one of ours. We remove the old tub, handle the plumbing, and install a new walk-in shower sized to your bathroom, usually in 1 to 3 days. You get a fixed-price quote before we start."),
            ("Built for New Orleans humidity", "Grout lines are where shower problems start in this climate: they trap moisture, grow mold, and need constant resealing. Our acrylic shower systems have no grout lines, so they stay cleaner with far less maintenance. We build with premium, American-made materials and back acrylic products with a lifetime guarantee."),
            # video inserts after index 2
            ("Safer, step-free options", "If you or someone in your home needs a safer shower, we install barrier-free and curbless showers with low or no thresholds, built-in seating, and grab bars. It is the same quality install, designed around easier, safer entry."),
            ("Fixed-price quotes, no surprises", "Older New Orleans homes sometimes hide outdated plumbing behind the walls. We tell you what your project needs and give you a fixed-price guaranteed quote before any work begins. No surprise change orders, no hidden fees."),
            ("Licensed, local, and guaranteed", "TurnKey Bath Remodel is locally owned and fully licensed and insured: Residential #890459, Commercial #3667. Every install is backed by a lifetime guarantee on acrylic and a 10-year workmanship guarantee, and it is part of why we hold a 4.9 Google rating with hundreds of five-star reviews."),
            ("What a new shower costs", "The price of a walk-in shower or a tub-to-shower conversion depends on the size of your shower, the materials you choose, and any plumbing updates your home needs. We give you a fixed-price guaranteed quote at your free consultation, and we offer 0% financing so it fits your budget."),
            ("Service area", "We serve Greater New Orleans and the surrounding metro, including Lakeview, Garden District, Uptown, Metairie, Mandeville, and the Northshore."),
        ],
        "video_after_index": 2,
        "faqs": [
            ("How much does a tub-to-shower conversion or walk-in shower cost in New Orleans?", "It depends on size, materials, and any plumbing work your home needs. You get a fixed-price guaranteed quote at your free consultation, with 0% financing available."),
            ("How long does a shower install take?", "Most shower replacements and tub-to-shower conversions are finished in 1 to 3 days."),
            ("Do you handle the old plumbing?", "Yes. We remove the old tub or shower, handle the plumbing, and install your new system. Anything your home needs is in your fixed-price quote."),
            ("Is acrylic better than tile in this climate?", "Acrylic has no grout lines to trap moisture or grow mold, so it stays cleaner with much less upkeep. That is a real advantage in New Orleans humidity. We will show you the options at your consultation."),
            ("Are you licensed and insured?", "Yes. Residential License #890459 and Commercial License #3667."),
        ],
        "closing": "Replace that old shower or finally lose the unused tub. Book your free in-home design consultation, a $250 value, or call our team now.",
        "ba_pairs": [
            ("images-ba/p2-ba1-before.jpg", "images-ba/p2-ba1-after.jpg", "Walk-in shower replacement"),
            ("images-ba/p2-ba2-before.jpg", "images-ba/p2-ba2-after.jpg", "Tub-to-shower conversion"),
        ],
    },
    "walk-in-tub-installation-new-orleans": {
        "slug": "walk-in-tub-installation-new-orleans",
        "title_tag": "Walk-In Tub Installation in New Orleans | TurnKey Bath",
        "meta_desc": "Safe, professionally installed walk-in tubs across New Orleans. Low step-in, built-in seat, grab bars. Free $250 consult, 0% financing. Call (504) 784-1784.",
        "h1": "Walk-In Tub Installation in New Orleans",
        "hero_img": "images-finished-bath/PHOTO-2023-11-14-12-50-49_c.jpg",
        "hero_img_alt": "Walk-in tub installation by TurnKey Bath Remodel — New Orleans",
        "badge": "Walk-In Tubs · Greater New Orleans",
        "subhead": "Safer, easier bathing for New Orleans homeowners. Professionally installed walk-in tubs with a low step-in, a built-in seat, and grab bars. Free $250 design consultation, 0% financing, and most installs finished in 1 to 3 days.",
        "above_fold_body": "If getting in and out of the tub has become a daily worry, a walk-in tub can make bathing safe and independent again. TurnKey Bath Remodel installs walk-in tubs across New Orleans with a low step-in threshold, a built-in seat, grab bars, and anti-slip flooring. We are a locally owned company that does only bathrooms, with a 4.9 Google rating and hundreds of five-star reviews. You work with one local team, get a fixed-price quote before we start, and most installs are finished in 1 to 3 days.",
        "video_src": "page3-video.mp4",
        "video_heading": "Safer bathing, professionally installed",
        "video_caption": "AI montage of recent walk-in tub installs by our New Orleans team.",
        "form_dropdown_options": ["Walk-in tub", "Walk-in tub with shower", "Bathtub replacement", "Not sure yet"],
        "sections": [
            ("Why a walk-in tub", "Most falls at home happen in the bathroom, and stepping over a high tub wall is one of the biggest risks. A walk-in tub replaces that step-over with a low, sealed door you walk through. Ours include a built-in seat, grab bars, anti-slip flooring, and easy-reach controls, so a bath is something to look forward to again, not something to fear."),
            ("Add a shower to your walk-in tub", "Prefer the option to shower as well as soak? We install walk-in tubs with a shower, so you get both in one space. We will walk you through the choices at your free consultation."),
            # video inserts after index 1
            ("Made to fit older New Orleans homes", "New Orleans bathrooms, especially in older and historic homes, can be tight. Because we are local and remodel these homes every week, we measure and plan your walk-in tub around your actual space during the free in-home consultation, so you know it fits before anything is ordered."),
            ("A local team, not a high-pressure national chain", "Walk-in tub buyers are often pressured by national companies that push a single inflated quote and a same-day discount. That is not how we work. TurnKey is locally owned, we give you a fixed-price guaranteed quote with no hidden fees, and a real person answers when you call. No scripts, no bait-and-switch."),
            ("Cost, financing, and Medicare", "A walk-in tub is a meaningful investment, and we are upfront about it. In most cases, Original Medicare does not cover walk-in tubs. We make it manageable with 0% financing and a fixed-price guaranteed quote, so you know the full cost before we begin and can spread it across flexible monthly payments."),
            ("Licensed, insured, and guaranteed", "TurnKey Bath Remodel is fully licensed and insured: Residential #890459, Commercial #3667. We back acrylic products with a lifetime guarantee and our work with a 10-year workmanship guarantee, and we bring 25 years of local experience to every install."),
            ("Also: standard bathtub replacement", "Not looking for a walk-in tub? We also replace standard bathtubs, with the same fixed-price quote and fast installation. Ask about it at your consultation."),
            ("Service area", "We serve Greater New Orleans and the surrounding metro, including Lakeview, Garden District, Uptown, Metairie, Mandeville, and the Northshore."),
        ],
        "video_after_index": 1,
        "faqs": [
            ("Does Medicare cover a walk-in tub?", "In most cases, Original Medicare does not cover walk-in tubs. We offer 0% financing and a fixed-price guaranteed quote so the cost fits your budget."),
            ("How much does a walk-in tub cost in New Orleans?", "It depends on the model and features you choose and your bathroom layout. You get a fixed-price guaranteed quote at your free consultation, with 0% financing available."),
            ("Will a walk-in tub fit in my older bathroom?", "Often, yes. We measure and plan around your actual space during the free in-home consultation, so it is confirmed before anything is ordered."),
            ("How long does installation take?", "Most walk-in tub installs are completed in 1 to 3 days."),
            ("Can I get a shower with my walk-in tub?", "Yes. We install walk-in tubs with a shower so you can soak or shower."),
            ("Are you licensed and insured?", "Yes. Residential License #890459 and Commercial License #3667."),
        ],
        "closing": "Make bathing safe and independent again. Book your free in-home design consultation, a $250 value, or call our team now.",
        "ba_pairs": [
            ("images-ba/p3-ba1-before.jpg", "images-ba/p3-ba1-after.jpg", "Walk-in tub install"),
            ("images-ba/p3-ba2-before.jpg", "images-ba/p3-ba2-after.jpg", "Walk-in tub with shower"),
        ],
    },
}


def render_form(page):
    opts = "".join(f'<option>{o}</option>' for o in page["form_dropdown_options"])
    return f'''<aside class="form-card" id="quote-form">
  <h2>{CTA_LABEL.capitalize()}</h2>
  <p class="form-sub">Free $250 in-home design consultation. No high-pressure sales.</p>
  <form onsubmit="event.preventDefault(); alert('Mock form — dev wires Gravity Forms on the live WP build.');">
    <label for="name">Full name *</label>
    <input id="name" type="text" required>
    <div class="form-row">
      <div>
        <label for="phone">Phone *</label>
        <input id="phone" type="tel" required>
      </div>
      <div>
        <label for="zip">ZIP code *</label>
        <input id="zip" type="text" required>
      </div>
    </div>
    <label for="email">Email (optional)</label>
    <input id="email" type="email">
    <label for="project">Project type *</label>
    <select id="project" required>
      <option value="">Select one...</option>
      {opts}
    </select>
    <button type="submit" class="submit-btn">{CTA_LABEL}</button>
    <p class="consent">By submitting, you agree to our <a href="https://www.turnkeybathremodel.com/privacy-policy/" target="_blank">privacy policy</a> and <a href="https://www.turnkeybathremodel.com/terms-and-conditions/" target="_blank">terms</a>. A real person answers, not a machine.</p>
    <p class="mock-note">MOCK FORM. Dev wires Gravity Forms (clone from /facebook-landing-page-duplicate/) on the live WP build.</p>
  </form>
</aside>'''


def cta_row(extra_class=""):
    return f'''<div class="cta-row {extra_class}">
    <a class="cta-call" href="{PHONE_HREF}">Call {PHONE_DISPLAY}</a>
    <a class="cta-quote" href="#quote-form">{CTA_LABEL}</a>
  </div>
  <p class="cta-microcopy">A real person answers, not a machine.</p>'''


def cta_strip():
    """Periodic inline CTA strip between body sections."""
    return f'''<section class="cta-strip">
  <div class="cta-strip-inner">
    <div class="cta-strip-text">
      <strong>Get your fixed-price quote.</strong>
      <span>Free in-home consultation worth $250. Most projects done in 1 to 3 days.</span>
    </div>
    <div class="cta-row">
      <a class="cta-call" href="{PHONE_HREF}">Call {PHONE_DISPLAY}</a>
      <a class="cta-quote" href="#quote-form">{CTA_LABEL}</a>
    </div>
  </div>
</section>'''


def render_video_block(data):
    return f'''<section class="video-block">
  <div class="video-inner">
    <h2>{data["video_heading"]}</h2>
    <p class="video-sub">{data["video_caption"]}</p>
    <div class="video-wrap">
      <video src="{data["video_src"]}" muted loop playsinline controls></video>
    </div>
  </div>
</section>'''


def render_ba_section(data):
    sliders = "".join(
        f'''<div class="ba-slider" data-ba-slider style="--pos: 50%;">
    <img class="ba-img ba-after-img" src="{after}" alt="{label} — after" draggable="false">
    <img class="ba-img ba-before-img" src="{before}" alt="{label} — before" draggable="false">
    <div class="ba-tag ba-tag-before">Before</div>
    <div class="ba-tag ba-tag-after">After</div>
    <div class="ba-handle" aria-hidden="true"></div>
    <div class="ba-label">{label}</div>
  </div>'''
        for before, after, label in data["ba_pairs"]
    )
    return f'''<section class="ba-section">
  <div class="ba-inner">
    <h2>Real transformations. Real Louisiana homeowners.</h2>
    <p class="ba-sub">Drag the handle to compare before and after.</p>
    <div class="ba-grid">{sliders}</div>
    <div class="ba-cta">
      <a class="cta-quote" href="#quote-form">{CTA_LABEL}</a>
    </div>
  </div>
</section>'''


def render_page(slug, data):
    bullets_html = "".join(f'<li>{b}</li>' for b in [
        "Free in-home design consultation, a $250 value, yours at no cost",
        "Fixed-price guaranteed quotes. No hidden fees, no surprises",
        "Licensed and insured. Residential #890459, Commercial #3667",
        "Most projects completed in 1 to 3 days",
        "0% financing available",
    ])

    # Body sections rendered single-column, with periodic CTA strip every 3 sections.
    # Video block inserts after data["video_after_index"].
    body_parts = []
    for i, (h, p) in enumerate(data["sections"]):
        body_parts.append(
            f'<section class="body-section"><div class="body-inner">'
            f'<h2>{h}</h2><p>{p}</p>'
            f'</div></section>'
        )
        # Insert video block at the spec-defined position
        if i == data["video_after_index"]:
            body_parts.append(render_video_block(data))
        # Insert periodic dual-CTA strip after every 3rd section (but not right next
        # to the video block, and not at the very end)
        if (i + 1) % 3 == 0 and i != data["video_after_index"] and i < len(data["sections"]) - 1:
            body_parts.append(cta_strip())
    sections_html = "".join(body_parts)

    faqs_html = "".join(
        f'<details class="faq-item"><summary>{q}</summary><div class="faq-answer">{a}</div></details>'
        for q, a in data["faqs"]
    )
    test_html = "".join(
        f'<div class="test-card"><div class="stars">★★★★★</div><p>"{quote}"</p><div class="author">{name}</div><div class="source">{src}</div></div>'
        for quote, name, src in TESTIMONIALS
    )

    ba_section_html = render_ba_section(data)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{data["title_tag"]}</title>
<meta name="description" content="{data["meta_desc"]}">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Public+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<!-- NAV -->
<nav class="nav-bar">
  <img class="logo" src="{LOGO}" alt="TurnKey Bath Remodel">
  <div class="nav-trust">
    <div class="nav-stars">★★★★★</div>
    <div class="nav-trust-text">4.9 Google Rating · Licensed &amp; Insured</div>
  </div>
  <div class="nav-right">
    <a class="nav-phone" href="{PHONE_HREF}">{PHONE_DISPLAY}</a>
    <a class="nav-cta-btn" href="#quote-form">{CTA_LABEL}</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <div class="hero-left">
      <div class="badge">{data["badge"]}</div>
      <h1>{data["h1"]}</h1>
      <img class="hero-mobile-img" src="{data["hero_img"]}" alt="{data["hero_img_alt"]}">
      <p class="subhead">{data["subhead"]}</p>
      <ul class="bullets">{bullets_html}</ul>
      {cta_row()}
      <div class="pullquote">
        <div class="stars">★★★★★</div>
        <p>"Beautiful work and finished a day early. The crew was clean, on-time, and the fixed price never changed."</p>
        <div class="author">— Robert White, New Orleans LA · Google Review</div>
      </div>
      <div class="cred-badges">
        <span class="cred-badge">Lifetime Warranty</span>
        <span class="cred-badge">LA Licensed &amp; Insured</span>
        <span class="cred-badge">0% Financing</span>
      </div>
    </div>
    {render_form(data)}
  </div>
</section>

<!-- TRUST BAR (4 stats per spec, count-up wiring stub) -->
<div class="trust-bar">
  <div class="trust-bar-inner">
    <div class="trust-item"><div class="num" data-count="500" data-suffix="+">500+</div><div class="label">Bathrooms Remodeled</div></div>
    <div class="trust-item"><div class="num" data-count="25" data-suffix="+ yrs">25+ yrs</div><div class="label">Experience</div></div>
    <div class="trust-item"><div class="num" data-count="4.9" data-suffix="★">4.9★</div><div class="label">Google Rating</div></div>
    <div class="trust-item"><div class="num" data-count="1" data-suffix="–3 days">1–3 days</div><div class="label">Most Installs</div></div>
  </div>
</div>

<!-- ABOVE FOLD BODY (paragraph + repeated CTA) -->
<section class="above-fold-body">
  <div class="above-fold-inner">
    <p>{data["above_fold_body"]}</p>
    {cta_row("center")}
  </div>
</section>

<!-- TESTIMONIALS (moved up per spec — directly after proof bar / above-fold) -->
<section class="testimonials">
  <div class="testimonials-inner">
    <h2>What New Orleans homeowners say</h2>
    <p class="test-sub">Real Google reviews from finished projects across the metro.</p>
    <div class="test-grid">{test_html}</div>
  </div>
</section>

<!-- BEFORE/AFTER SPLIT-SLIDER -->
{ba_section_html}

<!-- BODY SECTIONS (single-column, periodic CTA strips, video mid-page) -->
{sections_html}

<!-- FAQ -->
<section class="faq-block">
  <div class="faq-inner">
    <h2>Frequently asked questions</h2>
    <div class="faq-list">{faqs_html}</div>
  </div>
</section>

<!-- CLOSING CTA -->
<section class="closing-cta">
  <div class="closing-inner">
    <h2>{data["closing"]}</h2>
    {cta_row("center")}
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div class="nap">TurnKey Bath Remodel · 3436 Magazine St Suite 414-N, New Orleans, LA 70115 · <a href="{PHONE_HREF}">{PHONE_DISPLAY}</a></div>
  <div>
    <a href="https://www.turnkeybathremodel.com/privacy-policy/">Privacy Policy</a> ·
    <a href="https://www.turnkeybathremodel.com/terms-and-conditions/">Terms</a>
  </div>
  <p class="footer-meta">© 2026 TurnKey Bath Remodel · Residential License #890459 · Commercial License #3667</p>
</footer>

<!-- MOBILE STICKY BAR -->
<div class="mobile-bar">
  <a class="call" href="{PHONE_HREF}">Call Now</a>
  <a class="quote" href="#quote-form">{CTA_LABEL}</a>
</div>

<script>
// Before/After split-slider — pointerdown drag + click-to-jump
(function() {{
  const sliders = document.querySelectorAll('[data-ba-slider]');
  sliders.forEach(slider => {{
    const setPos = (clientX) => {{
      const rect = slider.getBoundingClientRect();
      let pct = ((clientX - rect.left) / rect.width) * 100;
      if (pct < 0) pct = 0;
      if (pct > 100) pct = 100;
      slider.style.setProperty('--pos', pct + '%');
    }};
    let active = false;
    slider.addEventListener('pointerdown', (e) => {{
      active = true;
      try {{ slider.setPointerCapture(e.pointerId); }} catch (_) {{}}
      setPos(e.clientX);
      e.preventDefault();
    }});
    slider.addEventListener('pointermove', (e) => {{
      if (!active) return;
      setPos(e.clientX);
    }});
    const release = (e) => {{
      active = false;
      try {{ slider.releasePointerCapture(e.pointerId); }} catch (_) {{}}
    }};
    slider.addEventListener('pointerup', release);
    slider.addEventListener('pointercancel', release);
    slider.addEventListener('pointerleave', (e) => {{ if (active) release(e); }});
  }});
}})();

// Proof-bar count-up on scroll-in
(function() {{
  const nums = document.querySelectorAll('.trust-item .num[data-count]');
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const isFloat = target % 1 !== 0;
      const duration = 1200;
      const start = performance.now();
      const step = (now) => {{
        const t = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - t, 3);
        const val = target * eased;
        el.textContent = (isFloat ? val.toFixed(1) : Math.round(val)) + suffix;
        if (t < 1) requestAnimationFrame(step);
      }};
      requestAnimationFrame(step);
      io.unobserve(el);
    }});
  }}, {{ threshold: 0.4 }});
  nums.forEach(n => io.observe(n));
}})();
</script>

</body>
</html>
'''

# Generate
out = Path(__file__).parent
for slug, data in PAGES.items():
    p = out / f"{slug}.html"
    p.write_text(render_page(slug, data), encoding="utf-8")
    print(f"  ok  {slug}.html  ({len(p.read_text(encoding='utf-8'))} bytes)")

# Build hub
hub = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TurnKey Bath — 3 PPC Landing Pages Mock</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Public+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Public Sans', sans-serif; background: #021f35; color: #fff; margin: 0; padding: 60px 24px; min-height: 100vh; }
  .wrap { max-width: 900px; margin: 0 auto; text-align: center; }
  h1 { font-family: 'Outfit', sans-serif; font-size: 38px; margin-bottom: 8px; }
  .sub { color: rgba(255,255,255,.7); margin-bottom: 40px; font-size: 16px; }
  .card-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
  .card { background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.15); border-radius: 12px; padding: 28px 22px; text-decoration: none; color: #fff; transition: transform .2s, background .2s; }
  .card:hover { transform: translateY(-4px); background: rgba(77,152,210,.18); }
  .card .num { font-family: 'Outfit', sans-serif; font-weight: 800; color: #4d98d2; font-size: 14px; margin-bottom: 8px; letter-spacing: 1px; }
  .card h2 { font-family: 'Outfit', sans-serif; font-size: 20px; margin-bottom: 10px; }
  .card p { font-size: 14px; color: rgba(255,255,255,.7); margin-bottom: 16px; }
  .card .open { color: #4d98d2; font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 14px; }
  .meta { margin-top: 50px; font-size: 13px; color: rgba(255,255,255,.55); line-height: 1.7; }
  .meta a { color: #4d98d2; }
  @media (max-width: 700px) { .card-grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
<div class="wrap">
  <h1>TurnKey Bath Remodel</h1>
  <p class="sub">3 paid-traffic landing pages, visual mock for Dimi &amp; Stephen.<br>Build target: beat <code>direct-cta-landing.lovable.app</code>.</p>
  <div class="card-grid">
    <a class="card" href="bathroom-remodeling-contractor.html">
      <div class="num">PAGE 1</div>
      <h2>Bathroom Remodeling Contractor</h2>
      <p>Full bathroom remodels, New Orleans metro.</p>
      <div class="open">View page →</div>
    </a>
    <a class="card" href="bathtub-and-shower-remodeling-contractor.html">
      <div class="num">PAGE 2</div>
      <h2>Bathtub &amp; Shower Remodeling</h2>
      <p>Walk-in showers, tub-to-shower conversions, barrier-free.</p>
      <div class="open">View page →</div>
    </a>
    <a class="card" href="walk-in-tub-installation-new-orleans.html">
      <div class="num">PAGE 3</div>
      <h2>Walk-In Tub Installation</h2>
      <p>Safer, low step-in bathing for seniors.</p>
      <div class="open">View page →</div>
    </a>
  </div>
  <div class="meta">
    <strong>Build target:</strong> turnkeybathremodel.com/facebook-landing-page-duplicate/ (functional base) + Lovable rhythm (visual mood) + Dimi's verbatim copy.<br><br>
    Phone: (504) 784-1784 · CallRail swap.js installed site-wide via GTM.<br>
    Forms are mock (do not submit). Live build uses Gravity Forms cloned from /facebook-landing-page-duplicate/.
  </div>
</div>
</body>
</html>
'''
(out / "index.html").write_text(hub, encoding="utf-8")
print(f"  ok  index.html (hub)")
print("\nDone.")
