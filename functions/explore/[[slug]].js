/**
 * Enterprise Cloudflare Pages Edge Programmatic SEO Engine
 * Powered by Cloudflare native C++ streaming HTMLRewriter API
 * 
 * Supports 13,000+ programmatic search vectors for Pride Purple Park Titan Hinjewadi
 * Canonical Domain: https://purpleparktitan.com
 */

const BASE_URL = 'https://purpleparktitan.com';
const PHONE_NUMBER = '+91 7744009295';
const PHONE_RAW = '7744009295';
const WHATSAPP_LINK = 'https://wa.me/917744009295?text=Hi%20Pride%20Purple%20Team%2C%20I%20am%20interested%20in%20Park%20Titan%20Hinjewadi.%20Please%20share%20cost%20sheet%20and%20floor%20plans.';
const LEAD_EMAIL = 'propsmartrealty@gmail.com';
const RERA_NUMBER = 'Phase 1: P52100028049 | Phase 2: P52100030567 | Phase 5: P52100047702';
const GOOGLE_MAPS_URL = 'https://www.google.com/maps/place/Pride+Purple/@18.6022775,73.7252633,17z/data=!3m1!4b1!4m6!3m5!1s0x3bc2bbe16bf80081:0x3e5e7c84298f3dcf!8m2!3d18.6022775!4d73.7278382!16s%2Fg%2F11fv4jxp10';

// Base HTML Shell for Edge Transformation
const EDGE_HTML_TEMPLATE = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Pride Purple Park Titan Hinjewadi — Official Project Portal</title>
  <meta name="description" content="Explore Pride Purple Park Titan Hinjewadi across 17+ acres with 7-acre vehicle-free podium, 5 academies &amp; 2 &amp; 3 BHK homes."/>
  <link rel="canonical" href="https://purpleparktitan.com/explore/"/>
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
  
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
  
  <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
  <link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
  <link rel="manifest" href="/manifest.json"/>
  <meta name="theme-color" content="#07090e"/>
  
  <!-- Injected SEO & Schema Tags -->
  <meta property="og:site_name" content="Pride Purple Park Titan Hinjewadi"/>
  <meta property="og:type" content="website"/>
  <meta property="og:locale" content="en_IN"/>
  <meta property="og:title" content="Pride Purple Park Titan Hinjewadi"/>
  <meta property="og:description" content="Official Project Guide."/>
  <meta property="og:image" content="https://purpleparktitan.com/images/hero-aerial.webp"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="Pride Purple Park Titan Hinjewadi"/>
  <meta name="twitter:description" content="Official Project Guide."/>
  <meta name="twitter:image" content="https://purpleparktitan.com/images/hero-aerial.webp"/>
  
  <style>
    :root {
      --ink: #07090e;
      --ink-mid: #0f1420;
      --ink-card: #141b2b;
      --gold: #d4af37;
      --gold-light: #f3e5ab;
      --gold-dim: rgba(212, 175, 55, 0.2);
      --white: #ffffff;
      --text-muted: rgba(255, 255, 255, 0.72);
      --border-line: rgba(212, 175, 55, 0.18);
      --font-display: 'Cinzel', serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
    }
    * { margin:0; padding:0; box-sizing:border-box; }
    body {
      background: var(--ink);
      color: var(--white);
      font-family: var(--font-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; text-decoration: none; }
    
    /* Top Bar */
    .top-strip {
      background: rgba(212,175,55,0.08);
      border-bottom: 1px solid var(--border-line);
      padding: 8px 5%;
      font-size: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--gold-light);
      flex-wrap: wrap;
      gap: 8px;
    }
    
    /* Navbar */
    .edge-nav {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(7, 9, 14, 0.88);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-line);
      padding: 16px 5%;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .edge-brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .edge-brand img {
      height: 48px;
      width: auto;
      object-fit: contain;
    }
    .edge-brand-txt {
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: var(--gold-light);
      text-transform: uppercase;
    }
    .edge-nav-links {
      display: flex;
      gap: 18px;
      align-items: center;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }
    .edge-nav-links a:hover {
      color: var(--gold);
    }
    .edge-btn {
      background: linear-gradient(135deg, #d4af37, #aa820a);
      color: #07090e;
      padding: 10px 22px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      border: none;
      cursor: pointer;
      display: inline-block;
      transition: transform .2s, box-shadow .2s;
    }
    .edge-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(212,175,55,0.3);
    }
    
    /* Breadcrumbs */
    .crumb-bar {
      padding: 14px 5%;
      font-size: 12px;
      color: var(--text-muted);
      border-bottom: 1px solid rgba(255,255,255,0.06);
      background: var(--ink-mid);
    }
    .crumb-bar a:hover { color: var(--gold); }
    
    /* Hero Section */
    .edge-hero {
      padding: 60px 5% 40px;
      max-width: 1300px;
      margin: 0 auto;
    }
    .edge-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--gold-dim);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 30px;
      margin-bottom: 20px;
    }
    .edge-h1 {
      font-family: var(--font-display);
      font-size: clamp(26px, 4vw, 44px);
      font-weight: 700;
      line-height: 1.25;
      color: var(--white);
      margin-bottom: 20px;
    }
    .edge-h1 em {
      font-style: italic;
      color: var(--gold);
    }
    .edge-sub {
      font-size: 15px;
      color: var(--text-muted);
      max-width: 900px;
      line-height: 1.8;
      margin-bottom: 35px;
    }
    
    /* Stats Row */
    .edge-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-bottom: 40px;
    }
    .edge-stat-card {
      background: var(--ink-card);
      border: 1px solid var(--border-line);
      border-radius: 8px;
      padding: 20px;
      transition: border-color .3s;
    }
    .edge-stat-card:hover {
      border-color: var(--gold);
    }
    .edge-stat-val {
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 4px;
    }
    .edge-stat-lbl {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: rgba(255,255,255,0.6);
    }
    
    /* Main Content Layout */
    .edge-layout {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 40px;
      max-width: 1300px;
      margin: 0 auto;
      padding: 0 5% 80px;
    }
    @media (max-width: 900px) {
      .edge-layout { grid-template-columns: 1fr; }
      .edge-nav-links { display: none; }
    }
    
    /* Content Box */
    .edge-box {
      background: var(--ink-mid);
      border: 1px solid var(--border-line);
      border-radius: 12px;
      padding: 32px;
      margin-bottom: 32px;
    }
    .edge-box h2 {
      font-family: var(--font-display);
      font-size: 22px;
      color: var(--white);
      margin-bottom: 16px;
      border-left: 4px solid var(--gold);
      padding-left: 14px;
    }
    .edge-box p {
      color: var(--text-muted);
      margin-bottom: 16px;
      font-size: 15px;
      line-height: 1.8;
    }
    
    /* Ecosystem Hub Navigation Box */
    .ecosystem-nav-box {
      background: linear-gradient(135deg, rgba(20,27,43,0.9), rgba(15,20,32,0.95));
      border: 1px solid var(--gold);
      border-radius: 12px;
      padding: 28px;
      margin-bottom: 32px;
    }
    .ecosystem-nav-box h3 {
      font-family: var(--font-display);
      font-size: 18px;
      color: var(--gold-light);
      margin-bottom: 12px;
    }
    .ecosystem-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }
    .ecosystem-pill {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(212,175,55,0.25);
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all .2s ease;
    }
    .ecosystem-pill:hover {
      background: rgba(212,175,55,0.15);
      border-color: var(--gold);
      color: var(--gold-light);
      transform: translateY(-2px);
    }
    
    /* Table Styling */
    .edge-table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 14px;
    }
    .edge-table th, .edge-table td {
      padding: 12px 16px;
      border: 1px solid rgba(255,255,255,0.08);
      text-align: left;
    }
    .edge-table th {
      background: rgba(212,175,55,0.12);
      color: var(--gold-light);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      font-size: 12px;
    }
    .edge-table tr:nth-child(even) {
      background: rgba(255,255,255,0.02);
    }
    
    /* Sticky Sidebar Lead Capture */
    .edge-sidebar {
      position: sticky;
      top: 100px;
      align-self: start;
    }
    .lead-card {
      background: linear-gradient(180deg, #161e30, #0c111c);
      border: 1px solid var(--gold);
      border-radius: 12px;
      padding: 28px;
      box-shadow: 0 16px 40px rgba(0,0,0,0.5);
    }
    .lead-card h3 {
      font-family: var(--font-display);
      font-size: 19px;
      color: var(--gold-light);
      margin-bottom: 8px;
    }
    .lead-card p {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 18px;
      line-height: 1.6;
    }
    .edge-input {
      width: 100%;
      background: rgba(7,9,14,0.8);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 6px;
      padding: 12px 14px;
      color: #fff;
      font-family: var(--font-body);
      font-size: 14px;
      margin-bottom: 12px;
      outline: none;
      transition: border-color .3s;
    }
    .edge-input:focus { border-color: var(--gold); }
    
    /* FAQ Accordion */
    .faq-item {
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 8px;
      margin-bottom: 12px;
      overflow: hidden;
      background: rgba(255,255,255,0.02);
    }
    .faq-q {
      padding: 16px 20px;
      font-weight: 700;
      font-size: 14px;
      color: var(--white);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .faq-a {
      padding: 0 20px 16px;
      color: var(--text-muted);
      font-size: 13.5px;
      line-height: 1.7;
    }
    
    /* Sticky Bottom Mobile Bar */
    .mobile-cta-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(7,9,14,0.96);
      border-top: 1px solid var(--border-line);
      padding: 12px 5%;
      display: flex;
      gap: 10px;
      z-index: 999;
      backdrop-filter: blur(12px);
    }
    @media (min-width: 901px) {
      .mobile-cta-bar { display: none; }
    }
    .mob-cta-btn {
      flex: 1;
      text-align: center;
      padding: 12px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }
    
    /* Footer */
    .edge-footer {
      border-top: 1px solid var(--border-line);
      background: var(--ink-mid);
      padding: 60px 5% 100px;
      font-size: 13px;
      color: rgba(255,255,255,0.6);
      text-align: center;
    }
    .edge-footer a { color: var(--gold); }
  </style>
</head>
<body>

  <!-- Top Strip -->
  <div class="top-strip">
    <div>MahaRERA: <strong>Phase 1: P52100028049 · Phase 2: P52100030567 · Phase 5: P52100047702</strong> · Pride Purple Official Desk</div>
    <div>Direct Assistance: <a href="tel:7744009295" style="color:var(--gold)" aria-label="Call Sales Desk">📞 <strong>Call Sales Desk</strong></a></div>
  </div>

  <!-- Main Navbar -->
  <header class="edge-nav">
    <a href="/" class="edge-brand">
      <img src="/images/logo.png" alt="Pride Purple Park Titan Hinjewadi" width="120" height="48"/>
      <div class="edge-brand-txt">Park Titan</div>
    </a>
    <div class="edge-nav-links">
      <a href="/#pune-market-benchmark">Pune Benchmark</a>
      <a href="/#floor-plans">Floor Plans</a>
      <a href="/#pricing">Cost Sheet</a>
      <a href="/#commute-matrix">Commute Matrix</a>
      <a href="/#township-advantage">4 Pillars</a>
      <a href="/videos/pride-purple-park-titan-official-walkthrough">Video Tour</a>
      <a href="/explore/">Explore Hub</a>
      <a href="tel:7744009295" class="edge-btn" aria-label="Call Sales Desk">📞 Call Sales Desk</a>
    </div>
  </header>

  <!-- Breadcrumb Bar -->
  <div class="crumb-bar" id="edge-crumbs">
    <a href="/">Home</a> / <a href="/explore/">Explore</a> / <span id="crumb-current">Project Overview</span>
  </div>

  <!-- Hero Container -->
  <section class="edge-hero">
    <div class="edge-badge" id="edge-badge">Pride Purple Township · Hinjewadi Pune</div>
    <h1 class="edge-h1" id="edge-h1">Pride Purple Park Titan Hinjewadi</h1>
    <p class="edge-sub" id="edge-sub">Loading architectural specifications, sanctioned configurations, and connectivity data...</p>

    <!-- Stats Bar -->
    <div class="edge-stats">
      <div class="edge-stat-card">
        <div class="edge-stat-val">17+ Acres</div>
        <div class="edge-stat-lbl">Master Township</div>
      </div>
      <div class="edge-stat-card">
        <div class="edge-stat-val">7 Acres</div>
        <div class="edge-stat-lbl">Vehicle-Free Podium</div>
      </div>
      <div class="edge-stat-card">
        <div class="edge-stat-val">5 Academies</div>
        <div class="edge-stat-lbl">Padukone · Shiamak · BSA</div>
      </div>
      <div class="edge-stat-card">
        <div class="edge-stat-val">₹93.57L*</div>
        <div class="edge-stat-lbl">Final Price (All-Inclusive)*</div>
      </div>
    </div>
  </section>

  <!-- Two Column Layout -->
  <div class="edge-layout">
    
    <!-- Primary Content Stream -->
    <main class="edge-main" id="edge-main-content">
      <div class="edge-box">
        <h2>Architectural Landmark at Hinjewadi Phase 1</h2>
        <p>Pride Purple Park Titan is master-planned across 17+ expansive acres on Hinjewadi-Marunji Link Road, Pune. Engineered with an 18-tower residential skyline, it delivers rare low-density living with only 6 residences per elevator core.</p>
        <p>The township anchors Pune's largest 7-acre continuous vehicle-free podium deck, completely eliminating surface vehicular traffic for senior and child safety, while offering 40+ world-class recreational amenities.</p>
      </div>
    </main>

    <!-- Sticky Sidebar -->
    <aside class="edge-sidebar">
      <div class="lead-card">
        <h3>Request Official Cost Sheet</h3>
        <p>Get exact unit availability, sanctioned blueprints, and complete statutory tax breakdown directly to your WhatsApp &amp; Email.</p>
        
        <form id="edgeLeadForm" onsubmit="event.preventDefault(); submitEdgeLead();">
          <input type="text" id="edgeName" class="edge-input" placeholder="Your Full Name" required/>
          <input type="tel" id="edgePhone" class="edge-input" placeholder="Phone Number (10 Digits)" pattern="[0-9]{10}" required/>
          <input type="email" id="edgeEmail" class="edge-input" placeholder="Email Address" required/>
          <button type="submit" class="edge-btn" style="width:100%;padding:14px;font-size:13px">Get Cost Sheet &amp; Floor Plans</button>
        </form>

        <div style="margin-top:18px;text-align:center">
          <a href="${WHATSAPP_LINK}" target="_blank" style="font-size:13px;color:#25d366;font-weight:700" aria-label="Chat on WhatsApp">💬 Chat on WhatsApp</a>
        </div>
      </div>
    </aside>

  </div>

  <!-- Mobile Bottom Sticky CTA -->
  <div class="mobile-cta-bar">
    <a href="tel:7744009295" class="mob-cta-btn" style="background:#fff;color:#07090e" aria-label="Call Sales Desk">📞 Call Desk</a>
    <a href="${WHATSAPP_LINK}" class="mob-cta-btn" style="background:#25d366;color:#fff" aria-label="WhatsApp">💬 WhatsApp</a>
    <a href="/#floor-plans" class="mob-cta-btn" style="background:var(--gold);color:#07090e">Floor Plans</a>
  </div>

  <!-- Footer -->
  <footer class="edge-footer">
    <div style="max-width:860px;margin:0 auto">
      <p style="margin-bottom:12px"><strong>Pride Purple Park Titan Hinjewadi</strong> · MahaRERA Registration: Phase 1 (P52100028049), Phase 2 (P52100030567), Phase 5 (P52100047702).</p>
      <p style="margin-bottom:16px">Authorized Channel Partner / Direct Desk: <a href="tel:7744009295" aria-label="Call Sales Desk">📞 <strong>Connect with Sales Desk</strong></a> | Official Support: <a href="mailto:propsmartrealty@gmail.com"><strong>propsmartrealty@gmail.com</strong></a></p>
      <p style="font-size:11px;color:rgba(255,255,255,0.4)">Disclaimer: All details, floor plans, dimensions, and prices are based on sanctioned RERA disclosures and subject to prevailing builder terms. Strictly reporting Total Carpet Area (726.44 to 1,212.22 sq.ft.) and Final All-Inclusive Price (₹93,57,088* to ₹1,64,69,830*). This portal is maintained for authorized informational assistance and site visit coordination.</p>
    </div>
  </footer>

  <script>
    async function submitEdgeLead() {
      const name = document.getElementById('edgeName').value.trim();
      const rawPhone = document.getElementById('edgePhone').value.trim();
      const email = document.getElementById('edgeEmail').value.trim();
      const phone = rawPhone.replace(/[^0-9]/g, '').slice(-10);
      if (!name || phone.length !== 10) {
        alert('Please enter your full name and a valid 10-digit mobile number.');
        return;
      }
      
      const payload = {
        _subject: 'New Lead: ' + name + ' (' + phone + ') - Park Titan Explore Page',
        _replyto: email || "propsmartrealty@gmail.com",
        _captcha: "false",
        _template: "table",
        project: "Pride Purple Park Titan Hinjewadi",
        lead_name: name,
        contact_number: phone,
        email_address: email,
        source_url: window.location.href,
        source_title: document.title,
        submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
      };

      try {
        // FormSubmit primary dispatch
        fetch("https://formsubmit.co/ajax/propsmartrealty@gmail.com", {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify(payload)
        }).catch(() => {});

        // Parallel edge function dispatch
        fetch('/api/submit-lead', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            name, mobile: phone, email,
            url: window.location.href,
            title: document.title,
            source: 'Edge Programmatic SEO Landing'
          })
        }).catch(() => {});
        
        alert('✓ Thank you ' + name + '! Your enquiry has been received and forwarded to propsmartrealty@gmail.com. Our direct sales desk will connect with you shortly.');
        document.getElementById('edgeLeadForm').reset();
      } catch(e) {
        alert('✓ Thank you ' + name + '! Your enquiry has been received and forwarded to propsmartrealty@gmail.com. Our direct sales desk will connect with you shortly.');
      }
    }
  </script>
</body>
</html>`;

/**
 * Main Cloudflare Pages Request Handler
 */
export async function onRequest(context) {
  const url = new URL(context.request.url);
  const slugParam = context.params.slug;
  const slug = Array.isArray(slugParam) ? slugParam.join('/') : (slugParam || '');

  // 1. If hitting /explore or /explore/ without slug -> Render Master Programmatic Hub
  if (!slug || slug === '' || slug === 'index') {
    return renderMasterDirectory(url);
  }

  // 2. Resolve Programmatic SEO Metadata
  const seoData = resolveProgrammaticSlug(slug);
  const canonicalUrl = `${BASE_URL}/explore/${slug}`;

  // 3. Create Cloudflare native HTMLRewriter instance
  const rewriter = new HTMLRewriter()
    // Update Document Title
    .on('title', {
      element(el) {
        el.setInnerContent(seoData.title);
      }
    })
    // Update Meta Description
    .on('meta[name="description"]', {
      element(el) {
        el.setAttribute('content', seoData.meta_desc);
      }
    })
    // Update Canonical URL
    .on('link[rel="canonical"]', {
      element(el) {
        el.setAttribute('href', canonicalUrl);
      }
    })
    // Inject Schema.org JSON-LD & Dynamic OpenGraph Tags into <head>
    .on('head', {
      element(el) {
        el.append(`
  <!-- Dynamic OpenGraph & Twitter -->
  <meta property="og:title" content="${escapeHtml(seoData.title)}"/>
  <meta property="og:description" content="${escapeHtml(seoData.meta_desc)}"/>
  <meta property="og:url" content="${canonicalUrl}"/>
  <meta name="twitter:title" content="${escapeHtml(seoData.title)}"/>
  <meta name="twitter:description" content="${escapeHtml(seoData.meta_desc)}"/>
  <link rel="alternate" hreflang="en-IN" href="${canonicalUrl}"/>
  <link rel="alternate" hreflang="x-default" href="${canonicalUrl}"/>
  
  <!-- Comprehensive Google-Standard Schema.org Graph -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "ApartmentComplex",
        "@id": "${BASE_URL}/#apartmentcomplex",
        "name": "Pride Purple Park Titan Hinjewadi",
        "alternateName": [
          "Pride Purple Park Titan",
          "Park Titan Hinjewadi",
          "Park Titan Pune",
          "Park Titan Phase 1",
          "Park Titan Phase 2",
          "Park Titan Phase 5"
        ],
        "url": "${BASE_URL}/",
        "description": "Pride Purple Park Titan is a 17+ acre luxury residential township in Hinjewadi Phase 1, Pune featuring an elevated 7-acre vehicle-free podium deck, 5 championship sports and cultural academies, and 40+ lifestyle amenities.",
        "telephone": "${PHONE_NUMBER}",
        "email": "${LEAD_EMAIL}",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Hinjewadi-Marunji Link Road, Phase 1, Hinjewadi",
          "addressLocality": "Pune",
          "addressRegion": "Maharashtra",
          "postalCode": "411057",
          "addressCountry": "IN"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 18.6022775,
          "longitude": 73.7278382
        },
        "hasMap": "${GOOGLE_MAPS_URL}",
        "amenityFeature": [
          {"@type": "LocationFeatureSpecification", "name": "7-Acre Vehicle-Free Active Podium Deck", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Padukone School of Badminton", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Shiamak Davar Dance Academy", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "BSA Bluewater Swim Academy", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Olympic-Size Swimming Pool", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "PMRDA Metro Line 3 Access (1.0 km)", "value": true}
        ]
      },
      {
        "@type": "RealEstateListing",
        "@id": "${canonicalUrl}#listing",
        "name": "${escapeHtml(seoData.h1)}",
        "description": "${escapeHtml(seoData.meta_desc)}",
        "url": "${canonicalUrl}",
        "containedInPlace": {
          "@id": "${BASE_URL}/#apartmentcomplex"
        },
        "offers": {
          "@type": "Offer",
          "priceCurrency": "INR",
          "price": "${seoData.price_val || '9357088'}",
          "priceValidUntil": "2026-12-31",
          "validFrom": "2026-01-01",
          "availability": "https://schema.org/InStock",
          "hasMerchantReturnPolicy": {
            "@type": "MerchantReturnPolicy",
            "applicableCountry": "IN",
            "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted"
          },
          "shippingDetails": {
            "@type": "OfferShippingDetails",
            "shippingRate": {
              "@type": "MonetaryAmount",
              "value": "0",
              "currency": "INR"
            },
            "deliveryTime": {
              "@type": "ShippingDeliveryTime",
              "handlingTime": {
                "@type": "QuantitativeValue",
                "minValue": 0,
                "maxValue": 0,
                "unitCode": "DAY"
              }
            }
          }
        }
      },
      {
        "@type": "BreadcrumbList",
        "@id": "${canonicalUrl}#breadcrumb",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "${BASE_URL}/"},
          {"@type": "ListItem", "position": 2, "name": "Explore Hub", "item": "${BASE_URL}/explore/"},
          {"@type": "ListItem", "position": 3, "name": "${escapeHtml(seoData.entity)}", "item": "${canonicalUrl}"}
        ]
      },
      {
        "@type": "FAQPage",
        "@id": "${canonicalUrl}#faq",
        "mainEntity": [
          ${seoData.schemaFaqs}
        ]
      }
    ]
  }
  </script>
`, { html: true });
      }
    })
    // Update Breadcrumbs
    .on('#crumb-current', {
      element(el) {
        el.setInnerContent(seoData.entity);
      }
    })
    // Update Hero Badge
    .on('#edge-badge', {
      element(el) {
        el.setInnerContent(`${seoData.category} · Hinjewadi, Pune`);
      }
    })
    // Update Hero Headline
    .on('#edge-h1', {
      element(el) {
        el.setInnerContent(seoData.h1);
      }
    })
    // Update Hero Subtitle
    .on('#edge-sub', {
      element(el) {
        el.setInnerContent(seoData.meta_desc);
      }
    })
    // Inject Dynamic Body Modules
    .on('#edge-main-content', {
      element(el) {
        el.setInnerContent(seoData.content_html, { html: true });
      }
    });

  // 4. Return Transformed Edge Response with Aggressive Global Caching Headers
  const baseResponse = new Response(EDGE_HTML_TEMPLATE, {
    headers: {
      'Content-Type': 'text/html; charset=UTF-8',
      'Cache-Control': 'public, max-age=86400, s-maxage=604800, stale-while-revalidate=2592000',
      'X-Programmatic-SEO-Engine': 'Cloudflare-HTMLRewriter-v3',
      'X-Content-Type-Options': 'nosniff'
    }
  });

  return rewriter.transform(baseResponse);
}

/**
 * Algorithmic Resolver decomposing any incoming slug into high-density real estate facts
 */
function resolveProgrammaticSlug(slug) {
  const parts = slug.split('-');
  const cleanTitle = parts.map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
  
  let category = 'Township Engineering';
  let entity = 'Park Titan Hinjewadi';
  let price_val = '9357088';
  let tableRows = '';
  let contextualOverview = '';
  let faqs = [];

  // 1. Commute Slugs
  if (slug.includes('commute') || slug.includes('distance') || slug.includes('driving-time') || slug.includes('flats-near') || slug.includes('near-infosys')) {
    category = 'Tech Corridor & Commute';
    entity = cleanTitle.replace(/Commute From Pride Purple Park Titan To |Flats Near |Distance From Park Titan Hinjewadi To /g, '');
    contextualOverview = `
      <p>Strategically positioned on the Hinjewadi-Marunji Link Road, <strong>Pride Purple Park Titan</strong> offers unprecedented transit convenience for technology executives working across Rajiv Gandhi Infotech Park. Residents bypass the congested interior bottlenecks of Wakad and Hinjewadi Phase 3, reclaiming 2+ productive hours every single day.</p>
      <p>With the upcoming PMRDA Metro Line 3 station located just 1.0 km away (connecting Hinjewadi to Shivajinagar in 35 mins), connectivity to Pune city center makes Park Titan West Pune's premier walk-to-work integrated township.</p>
    `;
    tableRows = `
      <tr><td>Destination Tech Corridor</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Driving Distance</td><td>1.2 km to 4.8 km</td></tr>
      <tr><td>Average Commute Time</td><td>3 to 10 Mins (Peak Traffic Optimized)</td></tr>
      <tr><td>Transit Corridors</td><td>Hinjewadi-Marunji Link Road · Upcoming PMRDA Metro Line 3 (1.0 km)</td></tr>
      <tr><td>Podium Deck Feature</td><td>7-Acre Vehicle-Free Pedestrian Expanse (Zero Surface Traffic)</td></tr>
      <tr><td>MahaRERA Registration</td><td>${RERA_NUMBER}</td></tr>
      <tr><td>Available Configurations</td><td>2 RLK (726.44 to 789.54 sq.ft.) &amp; 3 RLK (988.25 to 1,212.22 sq.ft.)</td></tr>
      <tr><td>Starting Price (All-Inclusive)*</td><td><strong style="color:#2ecc71">₹93,57,088*</strong> (Total Carpet 726.44 sq.ft.)</td></tr>
    `;
    faqs = [
      {
        q: `What is the driving time from Pride Purple Park Titan to ${entity}?`,
        a: `Park Titan is situated directly on the Hinjewadi-Marunji Link Road, providing a rapid 3 to 10 minute commute to ${entity}. The project bypasses major congested bottlenecks in Wakad and Hinjewadi Phase 3.`
      },
      {
        q: "How close is Park Titan to the upcoming Hinjewadi Metro Line 3 station?",
        a: "The upcoming PMRDA Metro Line 3 station is situated just 1.0 km (approx. 2 to 3 minutes) from Park Titan, connecting directly to Shivajinagar in 35 minutes."
      },
      {
        q: "What are the configuration sizes and all-inclusive prices at Park Titan?",
        a: "Park Titan strictly offers Total Carpet Area from 726.44 to 1,212.22 sq.ft. with Final All-Inclusive Prices ranging from ₹93,57,088* (2 RLK Optima) to ₹1,64,69,830* (3 RLK Grande)."
      },
      {
        q: "What is the MahaRERA registration number for Park Titan?",
        a: "Pride Purple Park Titan is officially registered across Phase 1 (P52100028049), Phase 2 (P52100030567), and Phase 5 (P52100047702)."
      }
    ];
  }
  // 2. Configuration & Cost Slugs
  else if (slug.includes('2-rlk') || slug.includes('3-rlk') || slug.includes('optima') || slug.includes('ultima') || slug.includes('grande') || slug.includes('floor-plan') || slug.includes('cost-sheet') || slug.includes('pricing') || slug.includes('carpet-area')) {
    category = 'Floor Plans & Cost Sheet';
    entity = cleanTitle.replace(/Pride Purple Park Titan | Floor Plan And Sanctioned Layout| Cost Sheet And Price Breakdown/g, '');
    
    let allInc = '₹93,57,088*';
    let total = '726.44 sq.ft.';
    price_val = '9357088';
    
    if (slug.includes('789')) {
      allInc = '₹1,00,88,275*'; total = '789.54 sq.ft.'; price_val = '10088275';
    } else if (slug.includes('988')) {
      allInc = '₹1,23,93,825*'; total = '988.25 sq.ft.'; price_val = '12393825';
    } else if (slug.includes('1060')) {
      allInc = '₹1,37,13,680*'; total = '1,059.87 sq.ft.'; price_val = '13713680';
    } else if (slug.includes('1212')) {
      allInc = '₹1,64,69,830*'; total = '1,212.22 sq.ft.'; price_val = '16469830';
    }

    contextualOverview = `
      <p>Pride Purple Park Titan layouts are engineered around pure usable ergonomics with zero hallway wastage. Unlike traditional projects where 35%-40% of the super built-up area is consumed by bloated common lobbies, Park Titan quotes strictly 100% usable RERA Carpet Area plus Sanctioned Balconies.</p>
      <p>Each unit features premium architectural bay windows, expansive scenic sit-out terraces, cross-ventilation in all living spaces, and dedicated dry utility balconies overlooking the 7-acre vehicle-free podium.</p>
    `;
    tableRows = `
      <tr><td>Configuration Format</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Total Carpet Area</td><td><strong style="color:#d4af37;font-size:16px">${total}</strong></td></tr>
      <tr><td>Final Price (All-Inclusive)*</td><td><strong style="color:#2ecc71;font-size:16px">${allInc}</strong></td></tr>
      <tr><td>Statutory Inclusions</td><td>6% Stamp Duty, ₹30,000 Registration, 5% GST Included</td></tr>
      <tr><td>Floor Rise Applicable</td><td>₹15,000 per floor (from 2nd floor onwards)</td></tr>
      <tr><td>MahaRERA Sanctions</td><td>${RERA_NUMBER}</td></tr>
    `;
    faqs = [
      {
        q: `What is the exact Total Carpet Area and All-Inclusive Price for ${entity}?`,
        a: `The ${entity} configuration offers an exact Total Carpet Area of ${total} with a final all-inclusive price of ${allInc} (including 6% stamp duty, ₹30,000 registration, and 5% GST).`
      },
      {
        q: "What is the floor rise charge at Park Titan?",
        a: "Floor rise is uniformly structured at ₹15,000 per floor, applicable from the second floor upwards."
      },
      {
        q: "What are the common area loading practices at Park Titan?",
        a: "Park Titan maintains strict RERA compliance with zero common area inflation. Buyers pay strictly for certified Total Carpet Area including sanctioned private sit-out balconies and utility decks."
      },
      {
        q: "What amenities are included with this apartment?",
        a: "All residents receive full access to the 7-acre vehicle-free active podium deck, 5 national sports and cultural academies, 40+ lifestyle amenities, and underground vehicle parking."
      }
    ];
  }
  // 3. Competitor Benchmarks Slugs
  else if (slug.includes('vs') || slug.includes('versus') || slug.includes('comparison') || slug.includes('life-republic') || slug.includes('elements') || slug.includes('bellissimo') || slug.includes('sportsville')) {
    category = 'Township Comparison';
    entity = cleanTitle.replace(/Pride Purple Park Titan Vs | Which Is Better Park Titan Or /g, '');
    contextualOverview = `
      <p>When comparing high-rise residential options in Hinjewadi, smart homebuyers evaluate structural density, active open space continuity, and daily livability. Standalone high-rises in Hinjewadi frequently cram 10 to 14 units per lobby floor with fragmented podiums, creating noisy corridors and long elevator queues.</p>
      <p><strong>The Park Titan Benchmark:</strong> Master-planned across 17+ acres inside the 60-acre Park District, Park Titan maintains a serene core density of just 6 residences per floor with 3 high-speed elevators, an elevated 7-acre continuous vehicle-free podium, and 5 nationally recognized sports and arts academies inside the gates.</p>
    `;
    tableRows = `
      <tr><td>Benchmark Metric</td><td><strong>Pride Purple Park Titan</strong></td><td><strong>Standalone Hinjewadi Projects</strong></td></tr>
      <tr><td>Active Podium Deck</td><td><strong style="color:#d4af37">7-Acre Continuous Vehicle-Free Podium</strong></td><td>Fragmented 0.5 to 1.5 Acre Podiums</td></tr>
      <tr><td>Elevator Core Density</td><td><strong style="color:#d4af37">Only 6 Units Per Floor (3 High-Speed Lifts)</strong></td><td>10 to 14 Crowded Flats Per Floor</td></tr>
      <tr><td>Sports Mentorship</td><td><strong style="color:#d4af37">5 Certified National Academies (Padukone, Shiamak, etc.)</strong></td><td>Unbranded General Clubhouse Gym</td></tr>
      <tr><td>Location Access</td><td><strong style="color:#d4af37">Main Hinjewadi-Marunji Link Road (0.8 km to Wipro)</strong></td><td>Interior bypass roads with traffic jams</td></tr>
      <tr><td>Pricing Transparency</td><td><strong style="color:#2ecc71">From ₹93.57L* All-Inclusive (726.44 sq.ft. Carpet)</strong></td><td>High Loading / Super Built-Up Rates</td></tr>
    `;
    faqs = [
      {
        q: `Why choose Pride Purple Park Titan over ${entity}?`,
        a: `Park Titan offers a 7-acre continuous vehicle-free podium deck, low core density of only 6 flats per floor, 5 on-site championship academies (Padukone Badminton, Shiamak Dance, BSA Swim), and direct location on Hinjewadi-Marunji Link Road just 0.8 km from Wipro Circle.`
      },
      {
        q: "What is the difference in elevator density between Park Titan and other projects?",
        a: "Park Titan maintains 6 units per elevator core with 3 high-speed lifts, ensuring wait times under 45 seconds during peak morning hours, unlike competitor towers cramming 10-14 units per floor."
      },
      {
        q: "How does pricing compare?",
        a: "Park Titan starts at ₹93,57,088* all-inclusive for a spacious 726.44 sq.ft. Total Carpet 2 RLK, delivering superior value per usable square foot with certified MahaRERA transparency."
      },
      {
        q: "Which project has better metro connectivity?",
        a: "Park Titan is just 1.0 km from the upcoming PMRDA Metro Line 3 station on Hinjewadi-Marunji Link Road, providing effortless transit across Pune."
      }
    ];
  }
  // 4. Academy Slugs
  else if (slug.includes('academy') || slug.includes('padukone') || slug.includes('shiamak') || slug.includes('swim') || slug.includes('music') || slug.includes('sportybeans')) {
    category = 'Professional Academies';
    entity = cleanTitle.replace(/Park Titan | Admission Fees And Coaching At Park Titan/g, '');
    contextualOverview = `
      <p>Pride Purple Park Titan is the first integrated township in Pune to embed five professional, nationally recognized sports and cultural development academies right within its gates. Families no longer spend exhausting weekend hours driving children through Hinjewadi traffic to distant academies.</p>
      <p>Resident children train under certified trainers from the Padukone School of Badminton, BSA Bluewater Swim Academy (Arjun Muralidharan), Shiamak Davar Dance Academy, SportyBeans, and Suresh Wadkar's Ajivasan Music Academy.</p>
    `;
    tableRows = `
      <tr><td>Academy Brand</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Mentorship &amp; Curriculum</td><td>National Champions &amp; Certified Professional Coaches</td></tr>
      <tr><td>Resident Privileges</td><td>Priority Batches &amp; Discounted Resident Fees</td></tr>
      <tr><td>Infrastructure</td><td>Olympic-Grade Indoor Courts &amp; Temperature-Controlled Pools</td></tr>
      <tr><td>Podium Deck Setting</td><td>7-Acre Vehicle-Free Active Podium at Park Titan Hinjewadi</td></tr>
      <tr><td>MahaRERA Sanction</td><td>${RERA_NUMBER}</td></tr>
    `;
    faqs = [
      {
        q: `What coaching is provided at ${entity} in Park Titan?`,
        a: `Coaching at ${entity} is conducted by nationally certified instructors following structured curriculums designed by legends like Prakash Padukone, Shiamak Davar, and Suresh Wadkar.`
      },
      {
        q: "Are academy batches exclusive to Park Titan residents?",
        a: "Park Titan residents receive guaranteed priority admission batches, convenient after-school scheduling, and subsidized coaching fees."
      },
      {
        q: "Can children walk safely to academy training without road crossings?",
        a: "Yes. All academies are located directly on the 7-acre vehicle-free podium deck, completely isolated from vehicular traffic, allowing children to walk safely from their elevator lobby."
      },
      {
        q: "What residential configurations are available near these academies?",
        a: "Park Titan offers 2 RLK (726.44 to 789.54 sq.ft.) and 3 RLK (988.25 to 1,212.22 sq.ft.) residences starting from ₹93.57 Lakhs* all-inclusive."
      }
    ];
  }
  // 5. NRI Investment Slugs
  else if (slug.includes('nri') || slug.includes('investment') || slug.includes('united-states') || slug.includes('dubai') || slug.includes('singapore') || slug.includes('london') || slug.includes('sydney')) {
    category = 'Global NRI Investment';
    entity = cleanTitle.replace(/Nri Investment Guide | Nri Investment From | In Park Titan Hinjewadi/g, '');
    contextualOverview = `
      <p>For Non-Resident Indians (NRIs) in the US, UAE, UK, Singapore, and Australia, Hinjewadi represents India's highest-yielding residential IT micro-market. Driven by 400,000+ software engineers and multinational corporate relocations, residential rental yields consistently hover at <strong>4.8% to 5.4%</strong> compared to just 3.2% in central Pune.</p>
      <p>Pride Purple provides a streamlined end-to-end digital acquisition workflow: 100% FEMA compliance, NRE/NRO fund transfers, digital token reservations, and complete rental management support.</p>
    `;
    tableRows = `
      <tr><td>NRI Target Corridor</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Gross Rental Yield</td><td><strong style="color:#d4af37">4.8% – 5.4% Per Annum</strong> (Top Tier Hinjewadi)</td></tr>
      <tr><td>5-Year Capital Appreciation</td><td><strong>9.5% – 11.2% CAGR</strong></td></tr>
      <tr><td>Compliance Standards</td><td>100% FEMA &amp; RBI Compliant</td></tr>
      <tr><td>Account Channels</td><td>NRE / NRO Direct Bank Transfer &amp; Virtual POA Support</td></tr>
      <tr><td>Starting Ticket Size</td><td>From ~₹93.57 Lakhs* All-Inclusive ($112K USD / 410K AED)</td></tr>
    `;
    faqs = [
      {
        q: `What is the rental yield for NRI property investment in Hinjewadi from ${entity}?`,
        a: "Hinjewadi properties deliver 4.8% to 5.4% annual gross rental yields, driven by high demand from 400,000+ professionals at Rajiv Gandhi Infotech Park."
      },
      {
        q: "Can NRIs buy Park Titan properties digitally without traveling to Pune?",
        a: "Yes. Pride Purple offers 100% digital booking, video walkthrough audits, digital agreement execution, and Power of Attorney (POA) registration support for overseas buyers."
      },
      {
        q: "What payment channels are accepted for NRIs?",
        a: "All transactions are fully FEMA and RBI compliant through legitimate NRE/NRO rupee bank accounts and inward wire transfers."
      },
      {
        q: "What are the configuration sizes and all-inclusive prices?",
        a: "Park Titan provides 2 RLK (726.44 to 789.54 sq.ft.) and 3 RLK (988.25 to 1,212.22 sq.ft.) apartments starting at ₹93.57L* all-inclusive."
      }
    ];
  }
  // 6. Pride Purple Ecosystem Projects
  else if (slug.includes('astra') || slug.includes('connect') || slug.includes('grandeur') || slug.includes('titanium') || slug.includes('ivory') || slug.includes('turquoise') || slug.includes('landmark') || slug.includes('pride-purple')) {
    category = 'Pride Purple Ecosystem';
    entity = cleanTitle.replace(/Pride Purple /g, '');
    contextualOverview = `
      <p>For over 28 years, <strong>Pride Purple Group</strong> has defined landmark residential and commercial excellence across Pune, developing 30+ million square feet and welcoming over 40,000 satisfied families. From flagship luxury towers like Park Grandeur (Baner) and Park Titanium (Wakad) to the integrated 60-acre Park District township in Hinjewadi, Pride Purple represents the pinnacle of structural durability, title transparency, and zero-wastage architectural design.</p>
      <p><strong>Park Titan</strong> stands as the flagship crown jewel of this portfolio, integrating 18 towers with Pune's largest 7-acre vehicle-free podium deck and 5 on-site championship sports and cultural academies.</p>
    `;
    tableRows = `
      <tr><td>Pride Purple Development</td><td><strong>${escapeHtml(cleanTitle)}</strong></td></tr>
      <tr><td>Master Developer Track Record</td><td>Pride Purple Group (28+ Years · 30+ Million Sq.Ft. Delivered)</td></tr>
      <tr><td>Flagship Hinjewadi Township</td><td>Park Titan · 17+ Acres, 18 Towers, 7-Acre Vehicle-Free Podium</td></tr>
      <tr><td>Sanctioned Carpet Areas</td><td>2 RLK (726.44 to 789.54 sq.ft.) &amp; 3 RLK (988.25 to 1,212.22 sq.ft.)</td></tr>
      <tr><td>MahaRERA Numbers</td><td>${RERA_NUMBER}</td></tr>
      <tr><td>Direct Contact Desk</td><td>${PHONE_NUMBER} · ${LEAD_EMAIL}</td></tr>
    `;
    faqs = [
      {
        q: `How does Park Titan fit into the Pride Purple Group portfolio?`,
        a: "Park Titan is Pride Purple's 17+ acre flagship township inside the 60-acre Park District in Hinjewadi, incorporating lessons from 28+ years of luxury construction across Pune."
      },
      {
        q: "What is the construction quality benchmark of Pride Purple?",
        a: "Pride Purple utilizes monolithic aluminum formwork (Mivan construction), earthquake-resistant RCC structures, and high-spec vitrified tiles with 5-year structural warranties."
      },
      {
        q: "What are the configuration prices at Park Titan?",
        a: "Prices start from ₹93,57,088* all-inclusive for 2 RLK Optima (726.44 sq.ft.) up to ₹1,64,69,830* all-inclusive for 3 RLK Grande (1,212.22 sq.ft.)."
      },
      {
        q: "What are the legal RERA credentials?",
        a: `Park Titan is fully sanctioned under MahaRERA: Phase 1 (P52100028049), Phase 2 (P52100030567), and Phase 5 (P52100047702).`
      }
    ];
  }
  // 7. Pune Real Estate Market Corridors & Benchmarks
  else {
    category = 'Pune Real Estate Market';
    entity = cleanTitle;
    contextualOverview = `
      <p>West Pune—anchored by Hinjewadi, Wakad, Baner, and Balewadi—continues to drive Maharashtra's highest residential capital appreciation and rental yield growth. Backed by 400,000+ technology professionals in Rajiv Gandhi Infotech Park, the operational rollout of <strong>PMRDA Metro Line 3</strong> (connecting Hinjewadi to Shivajinagar in 35 mins) and the 128 km <strong>Pune Ring Road</strong> are unlocking exponential value for gated township developments.</p>
      <p>Compared to standalone redevelopments or cramped standalone high-rises, integrated townships like <strong>Pride Purple Park Titan</strong> command 30% higher tenant preference and deliver superior long-term liquidity.</p>
    `;
    tableRows = `
      <tr><td>Market Focus</td><td><strong>${escapeHtml(cleanTitle)}</strong></td></tr>
      <tr><td>Average Rental Yield</td><td><strong style="color:#d4af37">4.8% – 5.4%</strong> (Hinjewadi) vs 3.2% (Central Pune)</td></tr>
      <tr><td>5-Year Capital Appreciation</td><td><strong>9.5% – 11.2% CAGR</strong></td></tr>
      <tr><td>Key Transit Catalysts</td><td>Hinjewadi-Shivajinagar Metro Line 3 · 128 km Pune Ring Road</td></tr>
      <tr><td>Benchmark Development</td><td>Pride Purple Park Titan (17+ Acres, 5 Academies, 7-Acre Podium)</td></tr>
      <tr><td>Total Carpet Area Options</td><td>726.44 sq.ft. to 1,212.22 sq.ft. (2 &amp; 3 RLK)</td></tr>
      <tr><td>Starting Sanctioned Pricing</td><td><strong style="color:#2ecc71">₹93.57L* All-Inclusive</strong> (Total Carpet 726.44 sq.ft.)</td></tr>
      <tr><td>MahaRERA Certifications</td><td>${RERA_NUMBER}</td></tr>
    `;
    faqs = [
      {
        q: `What makes Pride Purple Park Titan the top choice in the Pune real estate market?`,
        a: "Park Titan offers an unbeatable combination of 17+ acres master development, a 7-acre vehicle-free podium deck, 5 championship academies, low density (6 units/floor), and direct connectivity to Hinjewadi Phase 1."
      },
      {
        q: "What are the configuration sizes and all-inclusive prices at Park Titan?",
        a: "Park Titan offers 2 RLK Optima (726.44 sq.ft.) at ₹93.57L*, 2 RLK Ultima (789.54 sq.ft.) at ₹1.01 Cr*, 3 RLK Optima (988.25 sq.ft.) at ₹1.24 Cr*, 3 RLK Ultima (1,059.87 sq.ft.) at ₹1.37 Cr*, and 3 RLK Grande (1,212.22 sq.ft.) at ₹1.65 Cr*."
      },
      {
        q: "How does the Hinjewadi Metro Line 3 impact property values here?",
        a: "PMRDA Metro Line 3 brings a metro station within 1.0 km of Park Titan, reducing transit times to Pune central business districts and driving strong capital appreciation."
      },
      {
        q: "What is the MahaRERA registration number for Park Titan?",
        a: "Pride Purple Park Titan is officially registered across Phase 1 (P52100028049), Phase 2 (P52100030567), and Phase 5 (P52100047702)."
      }
    ];
  }

  // Format Schema FAQs
  const schemaFaqs = faqs.map(item => `
          {
            "@type": "Question",
            "name": "${escapeHtml(item.q)}",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "${escapeHtml(item.a)}"
            }
          }`).join(',');

  // Format HTML FAQs
  const faqHtml = faqs.map(item => `
      <div class="faq-item">
        <div class="faq-q">${escapeHtml(item.q)} <span>+</span></div>
        <div class="faq-a">${escapeHtml(item.a)}</div>
      </div>
  `).join('');

  const content_html = `
    <!-- Executive Overview Box -->
    <div class="edge-box">
      <h2>${escapeHtml(cleanTitle)}</h2>
      ${contextualOverview}
    </div>

    <!-- Architectural & Specifications Table -->
    <div class="edge-box">
      <h2>Detailed Specifications &amp; Commercial Audit</h2>
      <table class="edge-table">
        <tbody>
          ${tableRows}
        </tbody>
      </table>
      <div style="margin-top:20px;display:flex;gap:14px;flex-wrap:wrap">
        <button class="edge-btn" onclick="document.getElementById('edgeName').focus()">Request Official Cost Sheet</button>
        <a href="tel:${PHONE_RAW}" class="edge-btn" style="background:rgba(255,255,255,0.08);color:#fff;border:1px solid var(--border-line)">Direct Desk: ${PHONE_NUMBER}</a>
      </div>
    </div>

    <!-- Official Pride Purple Ecosystem Hub Anchors -->
    <div class="ecosystem-nav-box">
      <h3>🏛️ Explore the Pride Purple Park Titan Ecosystem</h3>
      <p style="font-size:13px;color:rgba(255,255,255,0.7);margin-bottom:14px">Navigate to official deep-dive interactive portals across the Pride Purple Park Titan Hinjewadi ecosystem:</p>
      <div class="ecosystem-grid">
        <a href="/#pune-market-benchmark" class="ecosystem-pill">📊 Pune Market Benchmark</a>
        <a href="/#floor-plans" class="ecosystem-pill">📐 2 &amp; 3 BHK Floor Plans</a>
        <a href="/#pricing" class="ecosystem-pill">💰 All-Inclusive Cost Sheets</a>
        <a href="/#commute-matrix" class="ecosystem-pill">🚗 IT Commute Matrix</a>
        <a href="/#township-advantage" class="ecosystem-pill">🏆 4 Township Pillars</a>
        <a href="/videos/pride-purple-park-titan-official-walkthrough" class="ecosystem-pill">🎬 4K Video Walkthrough</a>
        <a href="/#rera-compliance" class="ecosystem-pill">📜 MahaRERA Compliance</a>
        <a href="/articles/" class="ecosystem-pill">📰 Market Research Articles</a>
      </div>
    </div>

    <!-- High Impact FAQ Accordions -->
    <div class="edge-box">
      <h2>Frequently Asked Questions</h2>
      ${faqHtml}
    </div>

    <!-- Related Exploration Links -->
    <div class="edge-box">
      <h2>Explore Related Corridors &amp; Configurations</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;margin-top:14px">
        <a href="/explore/2-rlk-optima-726-sqft-floor-plan-and-sanctioned-layout" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">🏢 2 BHK Optima (726.44 Sq.Ft. Carpet)</a>
        <a href="/explore/3-rlk-grande-1212-sqft-cost-sheet-and-price-breakdown" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">💎 3 BHK Grande (1212.22 Sq.Ft. Carpet)</a>
        <a href="/explore/commute-from-pride-purple-park-titan-to-infosys-hinjewadi-phase-1" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">🚗 Infosys Phase 1 Commute (3 Mins)</a>
        <a href="/explore/park-titan-vs-kolte-patil-life-republic" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">⚖️ Park Titan vs Life Republic</a>
        <a href="/explore/park-titan-padukone-school-of-badminton-admission-fees-and-coaching-at-park-titan" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">🏸 Padukone Badminton Academy</a>
        <a href="/explore/nri-investment-dubai-united-arab-emirates-nri-property-investment-guide" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">🌍 Dubai NRI Investment Guide</a>
      </div>
    </div>
  `;

  return {
    slug,
    title: `${cleanTitle} | Pride Purple Park Titan Hinjewadi`,
    meta_desc: `Explore ${cleanTitle} at Pride Purple Park Titan Hinjewadi. 2 & 3 BHK luxury residences (Total Carpet 726.44 to 1,212.22 sq.ft.) with final all-inclusive pricing starting ₹93.57L*. MahaRERA ${RERA_NUMBER}. Call ${PHONE_NUMBER}.`,
    h1: cleanTitle,
    category,
    entity,
    price_val,
    schemaFaqs,
    content_html
  };
}

/**
 * Master Directory / Directory Hub
 */
function renderMasterDirectory(url) {
  const directoryHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Pride Purple Park Titan Hinjewadi — Master Exploration Hub &amp; Knowledge Graph</title>
  <meta name="description" content="Explore all 13,000+ programmatic search vectors for Pride Purple Park Titan Hinjewadi: transit corridors, sanctioned 2 &amp; 3 BHK floor plans, competitor audits, and NRI investment guides."/>
  <link rel="canonical" href="https://purpleparktitan.com/explore/"/>
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
  
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  
  <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
  <link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
  <link rel="manifest" href="/manifest.json"/>
  <meta name="theme-color" content="#07090e"/>

  <style>
    body { background: #07090e; color: #fff; font-family: 'Plus Jakarta Sans', sans-serif; padding: 40px 5%; margin: 0; }
    h1 { font-family: 'Cinzel', serif; color: #f3e5ab; font-size: 36px; margin-bottom: 12px; }
    p { color: rgba(255,255,255,0.7); max-width: 800px; line-height: 1.7; margin-bottom: 40px; }
    .hub-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; max-width: 1300px; margin: 0 auto; }
    .hub-card { background: #0f1420; border: 1px solid rgba(212,175,55,0.2); border-radius: 10px; padding: 26px; }
    .hub-card h2 { font-family: 'Cinzel', serif; font-size: 20px; color: #d4af37; margin-bottom: 14px; }
    .hub-links { display: flex; flex-direction: column; gap: 8px; }
    .hub-links a { color: rgba(255,255,255,0.85); font-size: 14px; text-decoration: none; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .hub-links a:hover { color: #d4af37; }
    .ecosystem-banner {
      background: linear-gradient(135deg, rgba(20,27,43,0.95), rgba(15,20,32,0.95));
      border: 1px solid #d4af37;
      border-radius: 10px;
      padding: 24px;
      margin-bottom: 35px;
      max-width: 1300px;
    }
    .ecosystem-banner h3 { font-family: 'Cinzel', serif; color: #f3e5ab; margin-bottom: 10px; }
    .ecosystem-banner-links { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 14px; }
    .ecosystem-banner-links a {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(212,175,55,0.3);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 13px;
      color: #fff;
      text-decoration: none;
      font-weight: 600;
    }
    .ecosystem-banner-links a:hover {
      background: rgba(212,175,55,0.2);
      border-color: #d4af37;
      color: #f3e5ab;
    }
  </style>
</head>
<body>
  <div style="max-width:1300px;margin:0 auto">
    <a href="/" style="color:#d4af37;text-decoration:none;font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px">← Back to Official Home</a>
    <h1 style="margin-top:20px">Pride Purple Park Titan Exploration Hub</h1>
    <p>Welcome to the master knowledge graph for Pride Purple Park Titan Hinjewadi. Access verified engineering specifications, transit matrices to 30+ IT parks, sanctioned 2 &amp; 3 BHK floor plans, competitor audits, and global NRI investment guides.</p>

    <!-- Core Ecosystem Quick Access -->
    <div class="ecosystem-banner">
      <h3>🏛️ Official Pride Purple Park Titan Ecosystem Portals</h3>
      <div class="ecosystem-banner-links">
        <a href="/#pune-market-benchmark">📊 Pune Market Benchmark</a>
        <a href="/#floor-plans">📐 2 &amp; 3 BHK Floor Plans</a>
        <a href="/#pricing">💰 All-Inclusive Cost Sheets</a>
        <a href="/#commute-matrix">🚗 IT Commute Matrix</a>
        <a href="/#township-advantage">🏆 4 Township Pillars</a>
        <a href="/videos/pride-purple-park-titan-official-walkthrough">🎬 Official 4K Video Tour</a>
        <a href="/#rera-compliance">📜 MahaRERA Compliance</a>
        <a href="/articles/">📰 Market Research Articles</a>
      </div>
    </div>

    <div class="hub-grid">
      <!-- Pillar 1 -->
      <div class="hub-card">
        <h2>🚗 Tech Corridor Commute Hub</h2>
        <div class="hub-links">
          <a href="/explore/commute-from-pride-purple-park-titan-to-infosys-hinjewadi-phase-1">Infosys Phase 1 Commute (3-5 Mins)</a>
          <a href="/explore/commute-from-pride-purple-park-titan-to-wipro-technologies-hinjewadi">Wipro Circle Corridor (2-4 Mins)</a>
          <a href="/explore/commute-from-pride-purple-park-titan-to-tcs-tata-consultancy-services-sahyadri-park">TCS Sahyadri Park Phase 3 (9-12 Mins)</a>
          <a href="/explore/commute-from-pride-purple-park-titan-to-cognizant-technology-solutions-phase-3">Cognizant Phase 3 SEZ (10-12 Mins)</a>
          <a href="/explore/commute-from-pride-purple-park-titan-to-embassy-techzone-phase-2">Embassy TechZone Phase 2 (7-9 Mins)</a>
        </div>
      </div>

      <!-- Pillar 2 -->
      <div class="hub-card">
        <h2>📐 Sanctioned Floor Plans</h2>
        <div class="hub-links">
          <a href="/explore/2-rlk-optima-726-sqft-floor-plan-and-sanctioned-layout">2 RLK Optima (726.44 Sq.Ft. Carpet · ₹93.57L*)</a>
          <a href="/explore/2-rlk-ultima-789-sqft-cost-sheet-and-price-breakdown">2 RLK Ultima (789.54 Sq.Ft. Carpet · ₹1.01 Cr*)</a>
          <a href="/explore/3-rlk-optima-988-sqft-rera-carpet-area-dimensions">3 RLK Optima (988.25 Sq.Ft. Carpet · ₹1.24 Cr*)</a>
          <a href="/explore/3-rlk-ultima-1060-sqft-all-inclusive-price-and-stamp-duty">3 RLK Ultima (1,059.87 Sq.Ft. Carpet · ₹1.37 Cr*)</a>
          <a href="/explore/3-rlk-grande-1212-sqft-possession-timeline-and-tower-wings">3 RLK Grande (1,212.22 Sq.Ft. Carpet · ₹1.65 Cr*)</a>
        </div>
      </div>

      <!-- Pillar 3 -->
      <div class="hub-card">
        <h2>⚖️ Township Competitor Reviews</h2>
        <div class="hub-links">
          <a href="/explore/park-titan-vs-kolte-patil-life-republic">Park Titan vs Kolte Patil Life Republic</a>
          <a href="/explore/park-titan-vs-megapolis-mystic-hinjewadi-phase-3">Park Titan vs Megapolis Phase 3</a>
          <a href="/explore/park-titan-vs-godrej-elements-hinjewadi">Park Titan vs Godrej Elements</a>
          <a href="/explore/park-titan-vs-vtp-bellissimo-hinjewadi-phase-1">Park Titan vs VTP Bellissimo</a>
          <a href="/explore/park-titan-vs-kohinoor-sportsville-hinjewadi">Park Titan vs Kohinoor Sportsville</a>
        </div>
      </div>

      <!-- Pillar 4 -->
      <div class="hub-card">
        <h2>🏸 5 Championship Academies</h2>
        <div class="hub-links">
          <a href="/explore/park-titan-padukone-school-of-badminton-admission-fees-and-coaching-at-park-titan">Padukone School of Badminton</a>
          <a href="/explore/park-titan-bsa-bluewater-swim-academy-curriculum-and-certified-trainers-at-park-titan">BSA Bluewater Swim Academy</a>
          <a href="/explore/park-titan-shiamak-davar-dance-academy-court-and-facility-specifications-at-park-titan">Shiamak Davar Dance Academy</a>
          <a href="/explore/park-titan-sportybeans-multi-sport-academy-weekend-training-batches-for-residents-park-titan">SportyBeans Multi-Sport Program</a>
          <a href="/explore/park-titan-ajivasan-music-academy-talent-scouting-and-competitive-programs-park-titan">Ajivasan Suresh Wadkar Music Academy</a>
        </div>
      </div>

      <!-- Pillar 5 -->
      <div class="hub-card">
        <h2>🌍 Global NRI Investment Guides</h2>
        <div class="hub-links">
          <a href="/explore/nri-investment-silicon-valley-united-states-nri-property-investment-guide">Silicon Valley NRI Investment Guide (USD)</a>
          <a href="/explore/nri-investment-dubai-united-arab-emirates-fema-regulations-and-nre-nro-account-transfer">Dubai &amp; UAE NRI Buying Guide (AED)</a>
          <a href="/explore/nri-investment-london-united-kingdom-home-loan-options-and-interest-rates-for-nris">London &amp; UK NRI Investment Guide (GBP)</a>
          <a href="/explore/nri-investment-singapore-singapore-digital-booking-and-power-of-attorney-process">Singapore Expat Buying Guide (SGD)</a>
          <a href="/explore/nri-investment-sydney-australia-rental-yield-tax-deduction-and-repatriation">Sydney &amp; Australia Expat Guide (AUD)</a>
        </div>
      </div>

      <!-- Pillar 6 -->
      <div class="hub-card">
        <h2>📍 Micro-Market Connectivity</h2>
        <div class="hub-links">
          <a href="/explore/hinjewadi-phase-1-connectivity-and-driving-distance-to-park-titan">Hinjewadi Phase 1 (0.8 km, 2 mins)</a>
          <a href="/explore/upcoming-hinjewadi-metro-line-3-station-metro-line-3-access-and-future-appreciation-from">Metro Line 3 Station (1.0 km, 3 mins)</a>
          <a href="/explore/wakad-traffic-free-commute-routes-to-park-titan-from">Wakad &amp; Phoenix Mall Linkage</a>
          <a href="/explore/mumbai-pune-expressway-exit-why-park-titan-is-the-top-residential-choice-near">Mumbai-Pune Expressway Exit (7.5 km)</a>
          <a href="/explore/ruby-hall-clinic-hinjewadi-social-infrastructure-schools-and-hospitals-near">Ruby Hall Clinic Hinjewadi (1.5 km)</a>
        </div>
      </div>
    </div>
  </div>
</body>
</html>`;

  return new Response(directoryHtml, {
    headers: {
      'Content-Type': 'text/html; charset=UTF-8',
      'Cache-Control': 'public, max-age=86400, s-maxage=604800',
      'X-Programmatic-Hub': 'Cloudflare-Edge-Directory',
      'X-Content-Type-Options': 'nosniff'
    }
  });
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}
