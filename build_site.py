#!/usr/bin/env python3
"""Generates the static GRIT site HTML files from shared templates.
Run: python3 build_site.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SEAL_SVG = '<img src="assets/img/grit-icon.png" alt="GRIT logo" class="brand-seal">'

def nav(active):
    def cls(key):
        return " class=\"active\"" if key == active else ""

    sectors_open_class = "active" if active == "sectors" else ""
    return f"""    <header class="site-header">
      <div class="nav-pill wrap" style="max-width:1180px;">
        <a href="index.html" class="brand">
          {SEAL_SVG}
          <span class="brand-sub">Resilient Infrastructure Task Force</span>
        </a>
        <button class="menu-toggle" aria-label="Toggle menu">
          <svg width="18" height="14" viewBox="0 0 18 14" fill="none"><path d="M0 1h18M0 7h18M0 13h18" stroke="white" stroke-width="2"/></svg>
        </button>
        <ul class="nav-links">
          <li{cls('home')}><a href="index.html">Home</a></li>
          <li{cls('about')}><a href="about.html">About GRIT</a></li>
          <li{cls('lifelines')}><a href="lifelines.html">Critical Lifelines</a></li>
          <li class="has-dropdown {sectors_open_class}">
            <button class="nav-link" type="button">Sectors
              <svg class="caret" viewBox="0 0 10 6" fill="none"><path d="M1 1l4 4 4-4" stroke="#171f44" stroke-width="1.6"/></svg>
            </button>
            <div class="dropdown-menu">
              <div class="dd-hint">Four critical lifelines</div>
              <a href="energy.html">Energy</a>
              <a href="water.html">Water</a>
              <a href="transportation.html">Transportation</a>
              <a href="communications.html">Communications</a>
            </div>
          </li>
          <li{cls('resources')}><a href="resources.html">Resources</a></li>
          <li class="nav-cta"><a href="resources.html" class="btn btn-navy">Get Prepared</a></li>
        </ul>
      </div>
    </header>
"""

def footer():
    return f"""    <footer class="site-footer">
      <div class="wrap">
        <div class="footer-grid">
          <div>
            <div class="footer-brand">
              {SEAL_SVG}
              <span>GRIT</span>
            </div>
            <p>The Governor's Resilient Infrastructure Task Force unites South Dakota's people, systems and partnerships to prepare for whatever comes next.</p>
          </div>
          <div>
            <h4>Explore</h4>
            <ul>
              <li><a href="about.html">About GRIT</a></li>
              <li><a href="lifelines.html">Critical Lifelines</a></li>
              <li><a href="resources.html">Resources</a></li>
            </ul>
          </div>
          <div>
            <h4>Sectors</h4>
            <ul>
              <li><a href="energy.html">Energy</a></li>
              <li><a href="water.html">Water</a></li>
              <li><a href="transportation.html">Transportation</a></li>
              <li><a href="communications.html">Communications</a></li>
            </ul>
          </div>
          <div>
            <h4>About This Site</h4>
            <ul>
              <li><a href="about.html#formed">How GRIT was formed</a></li>
              <li><a href="about.html#faq">FAQs</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <span>&copy; 2026 Governor's Resilient Infrastructure Task Force &middot; State of South Dakota</span>
          <span>Established by Executive Order 2025-06</span>
        </div>
      </div>
    </footer>
"""

def page(title, description, active, body, extra_head="", fragment=False):
    head = f"""  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="icon" href="assets/favicon/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="assets/favicon/favicon-192.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/favicon/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css" />
  {extra_head}"""

    content = f"""  <div class="draft-banner">DRAFT SITE — placeholder logo &amp; imagery, phase 2 sector pages coming soon. Not for public launch yet.</div>
{nav(active)}
{body}
{footer()}
  <script src="assets/script.js"></script>"""

    if fragment:
        # For the Artifact tool's entry file: no <!doctype>/<html>/<head>/<body> —
        # the platform wraps those itself. Title/meta/links go at the top.
        return head + "\n" + content + "\n"

    return f"""<!doctype html>
<html lang="en">
<head>
{head}
</head>
<body>
{content}
</body>
</html>
"""

def write(name, html):
    path = os.path.join(ROOT, name)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", name)


# ---------------------------------------------------------------------------
# Reusable icon set (inline SVG, stroke uses currentColor via CSS)
# ---------------------------------------------------------------------------
ICONS = {
    "energy": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></svg>',
    "water": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s7 7.2 7 12a7 7 0 0 1-14 0c0-4.8 7-12 7-12z"/></svg>',
    "transportation": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13l2-6a2 2 0 0 1 2-1.4h10A2 2 0 0 1 19 7l2 6M3 13v5a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h12v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-5M3 13h18M6.5 17.5h.01M17.5 17.5h.01"/></svg>',
    "communications": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 1 1 3.3 6.5L4 20l1.3-3.6A7.96 7.96 0 0 1 4 12z"/></svg>',
    "cyber": '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5.5v5.3c0 5 3.4 8.9 8 10.2 4.6-1.3 8-5.2 8-10.2V5.5L12 2z"/><path d="m9.5 12 1.8 1.8L15 10"/></svg>',
}

SECTOR_META = {
    "energy": {
        "label": "Energy",
        "teaser": "How South Dakota's power grid works, why it matters, and how to prepare for an outage.",
        "content": "How it works &middot; Why it matters &middot; Outage prep &middot; Partner spotlight",
        "lead": "Matt I.",
    },
    "water": {
        "label": "Water",
        "teaser": "Water and wastewater systems, storage basics, conservation, and emergency planning.",
        "content": "Water systems &middot; Storage &middot; Conservation &middot; Emergency planning",
        "lead": "Andy B.",
    },
    "transportation": {
        "label": "Transportation",
        "teaser": "Roads and supply chains, travel readiness, and winter travel safety across the state.",
        "content": "Roads &amp; supply chains &middot; Travel readiness &middot; Winter travel",
        "lead": "Craig Smith",
    },
    "communications": {
        "label": "Communications",
        "teaser": "911 systems, emergency alerts, family communication plans, and backup options.",
        "content": "911 &amp; alerts &middot; Family communication plans &middot; Backup options",
        "lead": "Jonathan / Perry",
    },
}

HERO_PATTERN = """<svg class="hero-pattern" viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#b3663a" stroke-opacity="0.18" fill="none" stroke-width="1.5">
    <path d="M-50 460 C 200 380, 380 520, 620 420 S 1050 300, 1260 380"/>
    <path d="M-50 520 C 220 440, 400 560, 660 480 S 1080 360, 1260 440"/>
    <path d="M-50 400 C 180 320, 360 460, 600 360 S 1020 240, 1260 320"/>
  </g>
  <g fill="#b3663a" fill-opacity="0.55">
    <circle cx="120" cy="120" r="2.4"/>
    <circle cx="260" cy="90" r="2.4"/>
    <circle cx="980" cy="140" r="2.4"/>
    <circle cx="1080" cy="200" r="2.4"/>
    <circle cx="760" cy="90" r="2.4"/>
    <circle cx="60" cy="300" r="2.4"/>
  </g>
  <g stroke="#ffffff" stroke-opacity="0.08" stroke-width="1">
    <line x1="0" y1="80" x2="1200" y2="80"/>
    <line x1="0" y1="160" x2="1200" y2="160"/>
  </g>
</svg>"""


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def index_body():
    return f"""
    <section class="hero">
      {HERO_PATTERN}
      <div class="wrap hero-inner">
        <div>
          <span class="eyebrow" style="color:#b3663a;">State of South Dakota</span>
          <h1>Strong systems. <span class="accent">Ready communities.</span> Resilient South Dakota.</h1>
          <p class="lead">GRIT unites the people who plan, operate and protect South Dakota's critical infrastructure — and helps every family and community get ready for whatever comes next.</p>
          <div class="hero-actions">
            <a href="about.html" class="btn btn-gold">Learn About GRIT</a>
            <a href="lifelines.html" class="btn btn-outline">Explore Critical Lifelines</a>
          </div>
        </div>
        <div class="hero-logo-card">
          <img src="assets/img/grit-logo-full.png" alt="GRIT — Governor's Resilient Infrastructure Task Force logo" />
          <span class="hero-logo-caption">Est. 2025 &middot; Executive Order 2025-06</span>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Getting Started</span>
          <h2>Three ways to get started</h2>
          <p>Whether you're here to learn, prepare or get involved, start wherever makes sense for you.</p>
        </div>
        <div class="card-grid">
          <div class="card">
            <div class="num">1</div>
            <h3>Learn the Lifelines</h3>
            <p>See the four systems South Dakota depends on — energy, water, transportation and communications — and how they connect.</p>
            <a href="lifelines.html" class="card-link">Explore Critical Lifelines →</a>
          </div>
          <div class="card">
            <div class="num">2</div>
            <h3>Build a Preparedness Plan</h3>
            <p>Start with a 72-hour kit, a family communication plan, and seasonal checklists built for South Dakota conditions.</p>
            <a href="resources.html" class="card-link">Get Prepared →</a>
          </div>
          <div class="card">
            <div class="num">3</div>
            <h3>Meet the Task Force</h3>
            <p>See who's behind GRIT, how it was formed, and the mission driving the work forward.</p>
            <a href="about.html" class="card-link">About GRIT →</a>
          </div>
        </div>

        <div class="seasonal">
          <div class="icon-wrap">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#b3663a" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M4.9 4.9l14.2 14.2M19.1 4.9 4.9 19.1M2 12h20M6 6l1.5 3M18 6l-1.5 3M6 18l1.5-3M18 18l-1.5-3"/></svg>
          </div>
          <div class="seasonal-copy">
            <h3>Winter preparedness starts now</h3>
            <p>Is your family ready for a South Dakota winter storm? Get the seasonal checklist before the first snow flies.</p>
          </div>
          <a href="resources.html" class="btn btn-gold">Get Ready →</a>
        </div>
      </div>
    </section>

    <section class="section-navy">
      <div class="wrap" style="max-width:820px;">
        <span class="eyebrow">Our Mission</span>
        <div class="mission-block">
          <p>&ldquo;To strengthen South Dakota's resilience by uniting the people who plan, operate and protect our critical infrastructure — assessing risk, guiding smart investment, and preparing our state to respond to disruption with determination, resilience and grit.&rdquo;</p>
        </div>
        <a href="about.html" class="btn btn-gold">Read the Full Story →</a>
      </div>
    </section>
"""


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def about_body():
    return f"""
    <section class="hero" style="padding-bottom:20px;">
      {HERO_PATTERN}
      <div class="wrap hero-inner" style="grid-template-columns: 1fr;">
        <div>
          <span class="eyebrow" style="color:#b3663a;">About</span>
          <h1>Resilience is a <span class="accent">shared responsibility.</span></h1>
          <p class="lead" style="max-width:60ch;">The Governor's Resilient Infrastructure Task Force (GRIT) brings together leaders and experts from across South Dakota to strengthen the critical systems our state relies on and help South Dakotans be better prepared when disruptions happen.</p>
          <p class="lead" style="max-width:60ch;">Because resilience isn't just about infrastructure. It's about making sure our families, communities and state are ready for whatever comes next.</p>
        </div>
      </div>
    </section>

    <section style="padding-top:50px;">
      <div class="wrap" style="max-width:820px;">
        <div class="note">
          <strong>Internal note (remove before launch):</strong> using &ldquo;Governor's Resilient Infrastructure Task Force&rdquo; throughout, matching the official logo and the original About GRIT draft. Flagging that press coverage of the executive order (and the order's own announcement) referred to it as the &ldquo;Governor's Resilience and Infrastructure Task Force&rdquo; — worth a quick confirm with comms that the logo/short name is the one to standardize on.
        </div>

        <h2>Strong systems. Ready communities. Resilient South Dakota.</h2>
        <span class="eyebrow">Mission</span>
        <div class="mission-block">
          <p>To strengthen South Dakota's resilience by uniting the people who plan, operate and protect our critical infrastructure — assessing risk, guiding smart investment, and preparing our state to respond to disruption with determination, resilience and grit.</p>
        </div>
        <p>GRIT is focused on strengthening South Dakota's resilience by bringing together the people responsible for the systems we depend on, identifying vulnerabilities and opportunities, and helping individuals, families and communities understand how they can play a role.</p>
        <p>That work centers on four critical lifelines: <strong>energy, water, transportation and communications</strong>, with cybersecurity woven throughout.</p>
        <a href="lifelines.html" class="btn btn-navy">Explore Critical Lifelines →</a>
      </div>
    </section>

    <section class="section-navy" id="formed">
      <div class="wrap" style="max-width:820px;">
        <span class="eyebrow">Background</span>
        <h2>How GRIT was formed</h2>
        <p>Governor Larry Rhoden established GRIT on June 2, 2025, through Executive Order 2025-06, directing the state to prepare for &ldquo;the most challenging circumstances&rdquo; with, in his words, &ldquo;determination, resilience, and grit.&rdquo;</p>
        <p>The task force is chaired by Lieutenant Governor Tony Venhuizen, with Adjutant General Mark Morrell serving as vice chair. Its members draw from state agencies, infrastructure operators and utilities, academic institutions, and subject-matter experts in cybersecurity and emergency management.</p>
        <p>GRIT's creation reflects a broader shift toward state-led preparedness — building South Dakota's own capacity to plan for, withstand and recover from disruptions to the systems residents depend on most.</p>
        <div class="note" style="background:rgba(179,102,58,0.1); border-color:#b3663a; color:rgba(255,255,255,0.85);">
          <strong style="color:#b3663a;">Internal note:</strong> press coverage of the signing date is inconsistent (reports range June 2&ndash;5, 2025). Used June 2 (earliest reporting) — confirm against the signed order before publishing.
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="section-head center" style="margin-left:auto;margin-right:auto;">
          <span class="eyebrow">Partnerships</span>
          <h2>Resilience takes all of us.</h2>
          <p>No single organization is responsible for South Dakota's resilience. GRIT brings together expertise from across the public and private sectors to better understand our risks, share knowledge and strengthen our collective preparedness.</p>
        </div>
        <div class="partner-grid">
          <div class="partner-card">
            <h4>Infrastructure &amp; Industry</h4>
            <p>The people who operate and maintain South Dakota's energy, water, transportation and communications systems.</p>
          </div>
          <div class="partner-card">
            <h4>State &amp; Local Government</h4>
            <p>Leaders and agencies responsible for planning, infrastructure, public safety and emergency response.</p>
          </div>
          <div class="partner-card">
            <h4>Federal Partners</h4>
            <p>Expertise and resources supporting infrastructure security and resilience.</p>
          </div>
          <div class="partner-card">
            <h4>Universities &amp; Research</h4>
            <p>Research, cybersecurity, technology and expertise that help South Dakota understand and prepare for emerging challenges.</p>
          </div>
        </div>
        <p style="margin-top:24px; font-size:0.88rem; font-style:italic;">Task force member list / partner logos — placeholder, pending headshots and bios.</p>
      </div>
    </section>

    <section class="section-navy" id="faq">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">FAQ</span>
          <h2>Frequently asked questions</h2>
        </div>
        <div class="faq-list">
          <details class="faq-item" open>
            <summary>What is GRIT? <span class="plus">+</span></summary>
            <div class="faq-body"><p>GRIT — the Governor's Resilient Infrastructure Task Force — brings together state, local, federal, industry and academic partners to strengthen South Dakota's critical infrastructure and help communities prepare for disruption.</p></div>
          </details>
          <details class="faq-item">
            <summary>What is critical infrastructure? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Content pending.</p></div>
          </details>
          <details class="faq-item">
            <summary>What are South Dakota's critical lifelines? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Energy, water, transportation and communications.</p></div>
          </details>
          <details class="faq-item">
            <summary>Why is cybersecurity part of GRIT? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Because technology connects and supports each critical lifeline, while cyber preparedness also affects individuals, families and businesses.</p></div>
          </details>
          <details class="faq-item">
            <summary>What does preparedness have to do with infrastructure resilience? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Content pending.</p></div>
          </details>
          <details class="faq-item">
            <summary>Who is part of GRIT? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Short answer + link/jump to members — pending.</p></div>
          </details>
          <details class="faq-item">
            <summary>How can I get involved? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Point people toward preparedness resources and partner materials rather than suggesting formal task-force participation.</p></div>
          </details>
          <details class="faq-item">
            <summary>How was GRIT formed? <span class="plus">+</span></summary>
            <div class="faq-body"><p>Governor Larry Rhoden created GRIT by executive order (2025-06) on June 2, 2025, appointing Lieutenant Governor Tony Venhuizen to chair the task force and Adjutant General Mark Morrell to serve as vice chair. See &ldquo;How GRIT was formed&rdquo; above for the fuller version.</p></div>
          </details>
        </div>
      </div>
    </section>
"""


# ---------------------------------------------------------------------------
# CRITICAL LIFELINES
# ---------------------------------------------------------------------------
def lifelines_body():
    cards = ""
    for key in ["energy", "water", "transportation", "communications"]:
        meta = SECTOR_META[key]
        cards += f"""
          <div class="lifeline-card">
            <div class="icon">{ICONS[key]}</div>
            <h3>{meta['label']}</h3>
            <p>{meta['teaser']}</p>
            <a href="{key}.html" class="tag">Sector page →</a>
          </div>"""

    return f"""
    <section class="stub-hero">
      <div class="wrap">
        <span class="eyebrow">Critical Lifelines</span>
        <h1>Four systems. One resilient South Dakota.</h1>
        <p>Our critical lifelines are the systems every South Dakotan depends on every day. GRIT works to understand how they connect, where the vulnerabilities are, and how to strengthen each one — with cybersecurity underpinning all four.</p>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="lifeline-stack">
          <svg class="cyber-connectors" aria-hidden="true"></svg>

          <div class="lifeline-grid">{cards}
          </div>

          <div class="cyber-card">
            <div class="icon">{ICONS['cyber']}</div>
            <div class="cyber-card-body">
              <h3>Cybersecurity — underpinning every lifeline</h3>
              <p>Cybersecurity isn't a fifth lifeline sitting apart from the other four — it's the layer that runs underneath and connects all of them. GRIT's work spans:</p>
              <div class="cyber-tags">
                <span class="tag">Operational Technology (OT) Cybersecurity</span>
                <span class="tag">Industrial Control Systems (ICS) Cybersecurity</span>
                <span class="tag">AI-Enabled Cybersecurity</span>
              </div>
            </div>
          </div>
        </div>

        <div class="note" style="margin-top:28px; max-width:760px;">
          Detailed sector pages (including the cybersecurity threads specific to each) are in development for Phase 2.
        </div>
      </div>
    </section>
"""


# ---------------------------------------------------------------------------
# RESOURCES
# ---------------------------------------------------------------------------
RESOURCE_ITEMS = [
    ("72-Hour Kit", "The basics every household should have on hand: water, food, light and first aid."),
    ("Family Communication Plan", "How to reach each other — and where to meet — if normal communication goes down."),
    ("Seasonal Preparedness", "Winter storms, severe weather and other South Dakota seasonal risks, checklist by checklist."),
    ("Financial Readiness", "Protecting records, documents and finances before disruption hits."),
    ("Pets &amp; Animals", "Preparedness planning for pets, livestock and working animals."),
    ("Downloads &amp; Printables", "Printable checklists, guides and planning worksheets to keep on hand."),
]

def resources_body():
    items = ""
    for title, desc in RESOURCE_ITEMS:
        items += f"""
          <li>
            <strong style="color:var(--navy-800); font-family:var(--font-head);">{title}</strong>
            <span class="stub-pill" style="margin-left:10px; padding:4px 12px; font-size:0.68rem;">Coming soon</span>
            <p style="margin:8px 0 0;">{desc}</p>
          </li>"""

    return f"""
    <section class="stub-hero">
      <div class="wrap">
        <span class="eyebrow">Resources</span>
        <h1>Get your family ready.</h1>
        <p>Practical, South-Dakota-specific preparedness resources — built with input from emergency management, public health and community partners.</p>
        <div class="stub-pill">Resource library in development</div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <ul class="stub-list">{items}
        </ul>
      </div>
    </section>
"""


# ---------------------------------------------------------------------------
# SECTOR STUBS
# ---------------------------------------------------------------------------
def sector_body(key):
    meta = SECTOR_META[key]
    return f"""
    <section class="stub-hero">
      <div class="wrap">
        <div class="crumb"><a href="lifelines.html">← Critical Lifelines</a></div>
        <span class="eyebrow">Sector</span>
        <h1>{meta['label']}</h1>
        <p>{meta['teaser']}</p>
        <div class="stub-pill">Phase 2 — page in development</div>
      </div>
    </section>

    <section>
      <div class="wrap" style="max-width:720px;">
        <h2>What this page will cover</h2>
        <p>{meta['content']}</p>
        <p style="font-size:0.85rem; font-style:italic;">Working lead: {meta['lead']}</p>
        <a href="lifelines.html" class="btn btn-navy">← Back to Critical Lifelines</a>
      </div>
    </section>
"""


def main():
    write("index.html", page(
        "GRIT — Governor's Resilient Infrastructure Task Force",
        "GRIT unites South Dakota's people, systems and partnerships to strengthen critical infrastructure and help communities prepare for disruption.",
        "home", index_body(),
    ))
    write("about.html", page(
        "About GRIT — Mission, Partnerships &amp; FAQs",
        "Learn about GRIT's mission, how the task force was formed, its partners, and answers to common questions.",
        "about", about_body(),
    ))
    write("lifelines.html", page(
        "Critical Lifelines — GRIT",
        "An introduction to South Dakota's four critical lifelines: energy, water, transportation and communications.",
        "lifelines", lifelines_body(),
    ))
    write("resources.html", page(
        "Resources — GRIT",
        "Preparedness resources for South Dakota families: 72-hour kits, family plans, seasonal prep and more.",
        "resources", resources_body(),
    ))
    for key in ["energy", "water", "transportation", "communications"]:
        meta = SECTOR_META[key]
        write(f"{key}.html", page(
            f"{meta['label']} — GRIT Sectors",
            meta["teaser"],
            "sectors", sector_body(key),
        ))

    # Artifact-publish entry point (fragment: no doctype/html/head/body —
    # the Artifact tool wraps those itself). Keeps index.html above intact
    # as a normal standalone file for the GitHub Pages zip.
    write("artifact-entry.html", page(
        "GRIT — Governor's Resilient Infrastructure Task Force",
        "GRIT unites South Dakota's people, systems and partnerships to strengthen critical infrastructure and help communities prepare for disruption.",
        "home", index_body(), fragment=True,
    ))


if __name__ == "__main__":
    main()
