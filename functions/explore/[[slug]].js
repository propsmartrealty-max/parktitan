/**
 * Enterprise Cloudflare Pages Edge Programmatic SEO Engine
 * Powered by Cloudflare native C++ streaming HTMLRewriter API
 * 
 * Supports 10,000+ programmatic search vectors for Pride Purple Park Titan Hinjewadi
 * Canonical Domain: https://purpleparktitan.com
 */

const BASE_URL = 'https://purpleparktitan.com';
const PHONE_NUMBER = '+91 7744009295';
const PHONE_RAW = '7744009295';
const WHATSAPP_LINK = 'https://wa.me/917744009295?text=Hi%20Pride%20Purple%20Team%2C%20I%20am%20interested%20in%20Park%20Titan%20Hinjewadi.%20Please%20share%20cost%20sheet%20and%20floor%20plans.';
const LEAD_EMAIL = 'propsmartrealty@gmail.com';
const RERA_NUMBER = 'P52100049631';

// Base HTML Shell for Edge Transformation
const EDGE_HTML_TEMPLATE = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Pride Purple Park Titan Hinjewadi — Official Project Portal</title>
  <meta name="description" content="Explore Pride Purple Park Titan Hinjewadi across 17+ acres with 7-acre vehicle-free podium, 5 academies &amp; 2 &amp; 3 BHK homes."/>
  <link rel="canonical" href="https://purpleparktitan.com/explore/"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
  <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
  <link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
  
  <!-- Injected SEO & Schema Tags -->
  <meta property="og:site_name" content="Pride Purple Park Titan Hinjewadi"/>
  <meta property="og:type" content="website"/>
  <meta property="og:title" content="Pride Purple Park Titan Hinjewadi"/>
  <meta property="og:description" content="Official Project Guide."/>
  <meta property="og:image" content="https://purpleparktitan.com/images/hero-aerial.webp"/>
  <meta name="twitter:card" content="summary_large_image"/>
  
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
    }
    
    /* Navbar */
    .edge-nav {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(7, 9, 14, 0.85);
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
      gap: 20px;
      align-items: center;
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
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
      padding: 70px 5% 50px;
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
      font-size: clamp(28px, 4.5vw, 48px);
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
      font-size: 16px;
      color: var(--text-muted);
      max-width: 880px;
      line-height: 1.8;
      margin-bottom: 35px;
    }
    
    /* Stats Row */
    .edge-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 50px;
    }
    .edge-stat-card {
      background: var(--ink-card);
      border: 1px solid var(--border-line);
      border-radius: 8px;
      padding: 22px;
      transition: border-color .3s;
    }
    .edge-stat-card:hover {
      border-color: var(--gold);
    }
    .edge-stat-val {
      font-family: var(--font-display);
      font-size: 26px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 4px;
    }
    .edge-stat-lbl {
      font-size: 12px;
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
      padding: 35px;
      margin-bottom: 35px;
    }
    .edge-box h2 {
      font-family: var(--font-display);
      font-size: 24px;
      color: var(--white);
      margin-bottom: 18px;
      border-left: 4px solid var(--gold);
      padding-left: 14px;
    }
    .edge-box p {
      color: var(--text-muted);
      margin-bottom: 18px;
      font-size: 15px;
      line-height: 1.8;
    }
    
    /* Table Styling */
    .edge-table {
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
      font-size: 14px;
    }
    .edge-table th, .edge-table td {
      padding: 14px 18px;
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
      padding: 30px;
      box-shadow: 0 16px 40px rgba(0,0,0,0.5);
    }
    .lead-card h3 {
      font-family: var(--font-display);
      font-size: 20px;
      color: var(--gold-light);
      margin-bottom: 8px;
    }
    .lead-card p {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 20px;
    }
    .edge-input {
      width: 100%;
      background: rgba(7,9,14,0.8);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 6px;
      padding: 14px 16px;
      color: #fff;
      font-family: var(--font-body);
      font-size: 14px;
      margin-bottom: 14px;
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
      padding: 18px 22px;
      font-weight: 700;
      font-size: 15px;
      color: var(--white);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .faq-a {
      padding: 0 22px 18px;
      color: var(--text-muted);
      font-size: 14px;
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
      gap: 12px;
      z-index: 999;
      backdrop-filter: blur(12px);
    }
    @media (min-width: 901px) {
      .mobile-cta-bar { display: none; }
    }
    .mob-cta-btn {
      flex: 1;
      text-align: center;
      padding: 12px 16px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
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
    <div>MahaRERA Reg: <strong>P52100049631</strong> · Pride Purple Group Official Desk</div>
    <div>Direct Assistance: <a href="tel:7744009295" style="color:var(--gold)"><strong>+91 7744009295</strong></a></div>
  </div>

  <!-- Main Navbar -->
  <header class="edge-nav">
    <a href="/" class="edge-brand">
      <img src="/images/logo.png" alt="Pride Purple Park Titan Hinjewadi" width="120" height="48"/>
      <div class="edge-brand-txt">Park Titan</div>
    </a>
    <div class="edge-nav-links">
      <a href="/#specs">Township</a>
      <a href="/#floor-plans">Floor Plans</a>
      <a href="/#pricing">Cost Sheet</a>
      <a href="/#township-advantage">4 Pillars</a>
      <a href="/explore/">Explore Hub</a>
      <a href="tel:7744009295" class="edge-btn">Call 7744009295</a>
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
        <div class="edge-stat-val">₹84.02L*</div>
        <div class="edge-stat-lbl">Starting Agreement Value</div>
      </div>
    </div>
  </section>

  <!-- Two Column Layout -->
  <div class="edge-layout">
    
    <!-- Primary Content Stream -->
    <main class="edge-main" id="edge-main-content">
      <div class="edge-box">
        <h2>Architectural Masterpiece at Hinjewadi Phase 1</h2>
        <p>Pride Purple Park Titan is master-planned across 17+ expansive acres in Hinjewadi-Marunji Link Road, Pune. Engineered with an 18-tower residential skyline, it delivers rare low-density living with only 6 residences per elevator core.</p>
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

        <div style="margin-top:20px;text-align:center">
          <a href="${WHATSAPP_LINK}" target="_blank" style="font-size:13px;color:#25d366;font-weight:700">💬 Chat on WhatsApp (+91 7744009295)</a>
        </div>
      </div>
    </aside>

  </div>

  <!-- Mobile Bottom Sticky CTA -->
  <div class="mobile-cta-bar">
    <a href="tel:7744009295" class="mob-cta-btn" style="background:#fff;color:#07090e">📞 Call Desk</a>
    <a href="${WHATSAPP_LINK}" class="mob-cta-btn" style="background:#25d366;color:#fff">💬 WhatsApp</a>
    <a href="/#floor-plans" class="mob-cta-btn" style="background:var(--gold);color:#07090e">Floor Plans</a>
  </div>

  <!-- Footer -->
  <footer class="edge-footer">
    <div style="max-width:800px;margin:0 auto">
      <p style="margin-bottom:12px"><strong>Pride Purple Park Titan Hinjewadi</strong> · MahaRERA Registration: P52100049631, P52100080502, P52100031768, P52100034961.</p>
      <p style="margin-bottom:16px">Authorized Channel Partner / Direct Desk: <a href="tel:7744009295"><strong>+91 7744009295</strong></a> | Enquiries: <a href="mailto:propsmartrealty@gmail.com"><strong>propsmartrealty@gmail.com</strong></a></p>
      <p style="font-size:11px;color:rgba(255,255,255,0.4)">Disclaimer: All details, floor plans, dimensions, and prices are based on sanctioned RERA disclosures and subject to prevailing builder terms. This portal is maintained for authorized informational assistance and site visit coordination.</p>
    </div>
  </footer>

  <script>
    async function submitEdgeLead() {
      const name = document.getElementById('edgeName').value.trim();
      const phone = document.getElementById('edgePhone').value.trim();
      const email = document.getElementById('edgeEmail').value.trim();
      if (!name || !phone) return;
      
      try {
        const payload = {
          name, phone, email,
          url: window.location.href,
          title: document.title,
          source: 'Edge Programmatic SEO Landing'
        };
        fetch('/api/submit-lead', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(payload)
        }).catch(() => {});
        
        alert('Thank you ' + name + '! Your request has been received. Our Park Titan specialist will connect with you shortly at ' + phone + '.');
      } catch(e) {
        alert('Thank you! Our sales desk (+91 7744009295) has received your request.');
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
        el.setAttribute('href', `${BASE_URL}/explore/${slug}`);
      }
    })
    // Inject Schema.org JSON-LD & Dynamic OpenGraph Tags into <head>
    .on('head', {
      element(el) {
        el.append(`
  <!-- Dynamic OpenGraph & Twitter -->
  <meta property="og:title" content="${escapeHtml(seoData.title)}"/>
  <meta property="og:description" content="${escapeHtml(seoData.meta_desc)}"/>
  <meta property="og:url" content="${BASE_URL}/explore/${slug}"/>
  
  <!-- Schema.org Graph -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "RealEstateListing",
        "name": "${escapeHtml(seoData.h1)}",
        "description": "${escapeHtml(seoData.meta_desc)}",
        "url": "${BASE_URL}/explore/${slug}",
        "offers": {
          "@type": "Offer",
          "priceCurrency": "INR",
          "price": "${seoData.price_val || '8402750'}",
          "availability": "https://schema.org/InStock",
          "validFrom": "2026-01-01"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "${BASE_URL}/"},
          {"@type": "ListItem", "position": 2, "name": "Explore", "item": "${BASE_URL}/explore/"},
          {"@type": "ListItem", "position": 3, "name": "${escapeHtml(seoData.entity)}", "item": "${BASE_URL}/explore/${slug}"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What are the configuration sizes and prices at Pride Purple Park Titan?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Park Titan offers 2 RLK (726 to 789 sq.ft.) starting ₹84.02 Lakhs* agreement value and 3 RLK (988 to 1,212 sq.ft.) starting ₹1.11 Cr* agreement value. All-inclusive costs include 6% stamp duty, ₹30,000 registration, and 5% GST."
            }
          },
          {
            "@type": "Question",
            "name": "How far is Pride Purple Park Titan from Hinjewadi Phase 1?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Park Titan is located right on the Hinjewadi-Marunji Link Road, just 0.8 km to 1.5 km (2 to 5 minutes) from Wipro Circle and Hinjewadi Phase 1 IT Park."
            }
          },
          {
            "@type": "Question",
            "name": "What is the MahaRERA registration number for Park Titan?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Pride Purple Park Titan is sanctioned under MahaRERA registration numbers P52100049631, P52100080502, P52100031768, and P52100034961."
            }
          },
          {
            "@type": "Question",
            "name": "What sports academies are located inside Park Titan?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The project features 5 premier national academies: Padukone School of Badminton, BSA Bluewater Swim Academy, Shiamak Davar Dance Academy, SportyBeans, and Ajivasan Music Academy."
            }
          }
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
      'X-Programmatic-SEO-Engine': 'Cloudflare-HTMLRewriter-v2'
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
  let price_val = '8402750';
  let tableRows = '';
  let contextualOverview = '';

  // 1. Commute Slugs
  if (slug.includes('commute') || slug.includes('distance') || slug.includes('driving-time') || slug.includes('flats-near')) {
    category = 'Tech Corridor & Commute';
    entity = cleanTitle.replace(/Commute From Pride Purple Park Titan To |Flats Near |Distance From Park Titan Hinjewadi To /g, '');
    contextualOverview = `
      <p>Strategically positioned on the Hinjewadi-Marunji Link Road, <strong>Pride Purple Park Titan</strong> offers unprecedented transit convenience for technology executives working across Rajiv Gandhi Infotech Park. Residents bypass the congested interior bottlenecks of Wakad and Hinjewadi Phase 3, reclaiming 2+ productive hours every single day.</p>
      <p>With the upcoming PMRDA Metro Line 3 station located just 1.0 km away, connectivity to Pune city center (Shivajinagar in 35 mins) makes Park Titan West Pune's premier walk-to-work integrated township.</p>
    `;
    tableRows = `
      <tr><td>Destination Tech Hub</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Driving Distance</td><td>1.2 km to 4.8 km</td></tr>
      <tr><td>Average Commute Time</td><td>3 to 10 Mins (Peak Traffic Optimized)</td></tr>
      <tr><td>Transit Corridors</td><td>Hinjewadi-Marunji Link Road · Upcoming Metro Line 3</td></tr>
      <tr><td>Podium Deck Feature</td><td>7-Acre Vehicle-Free Pedestrian Expanse</td></tr>
      <tr><td>Sanctioned RERA</td><td>${RERA_NUMBER} (Phase V Sanctions Verified)</td></tr>
    `;
  }
  // 2. Configuration & Cost Slugs
  else if (slug.includes('2-rlk') || slug.includes('3-rlk') || slug.includes('optima') || slug.includes('ultima') || slug.includes('grande') || slug.includes('floor-plan')) {
    category = 'Floor Plans & Cost Sheet';
    entity = cleanTitle.replace(/Pride Purple Park Titan | Floor Plan And Sanctioned Layout| Cost Sheet And Price Breakdown/g, '');
    
    let agVal = '₹84,02,750';
    let allInc = '₹93,57,088*';
    let carpet = '652.45 sq.ft.';
    let balcony = '73.99 sq.ft.';
    let total = '726.44 sq.ft.';
    
    if (slug.includes('789')) {
      agVal = '₹90,61,500'; allInc = '₹1,00,88,275*'; carpet = '680.14 sq.ft.'; balcony = '109.40 sq.ft.'; total = '789.54 sq.ft.'; price_val = '9061500';
    } else if (slug.includes('988')) {
      agVal = '₹1,11,38,500'; allInc = '₹1,23,93,825*'; carpet = '906.40 sq.ft.'; balcony = '81.85 sq.ft.'; total = '988.25 sq.ft.'; price_val = '11138500';
    } else if (slug.includes('1060')) {
      agVal = '₹1,23,27,600'; allInc = '₹1,37,13,680*'; carpet = '936.17 sq.ft.'; balcony = '123.70 sq.ft.'; total = '1,059.87 sq.ft.'; price_val = '12327600';
    } else if (slug.includes('1212')) {
      agVal = '₹1,48,10,600'; allInc = '₹1,64,69,830*'; carpet = '1,063.46 sq.ft.'; balcony = '148.76 sq.ft.'; total = '1,212.22 sq.ft.'; price_val = '14810600';
    }

    contextualOverview = `
      <p>Pride Purple Park Titan layouts are engineered around pure usable ergonomics with zero hallway wastage. Unlike traditional projects where 35%-40% of the super built-up area is consumed by common lobbies, Park Titan quotes strictly 100% usable RERA Carpet Area plus Sanctioned Balconies.</p>
      <p>Each unit features premium architectural bay windows, expansive scenic sit-out terraces, cross-ventilation in all living spaces, and dedicated dry utility balconies.</p>
    `;
    tableRows = `
      <tr><td>Configuration Format</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Net RERA Usable Carpet</td><td>${carpet}</td></tr>
      <tr><td>Sanctioned Balcony Area</td><td>${balcony}</td></tr>
      <tr><td>Total Sanctioned Living Space</td><td><strong>${total}</strong></td></tr>
      <tr><td>Agreement Value</td><td><strong>${agVal}</strong></td></tr>
      <tr><td>All-Inclusive Total (Taxes Incl.)</td><td><strong style="color:#d4af37">${allInc}</strong></td></tr>
      <tr><td>Floor Rise Applicable</td><td>₹15,000 per floor (from 2nd floor onwards)</td></tr>
      <tr><td>MahaRERA Sanction Status</td><td>Registered &amp; Fully Sanctioned (${RERA_NUMBER})</td></tr>
    `;
  }
  // 3. Competitor Slugs
  else if (slug.includes('vs') || slug.includes('versus') || slug.includes('comparison')) {
    category = 'Township Comparison';
    entity = cleanTitle.replace(/Pride Purple Park Titan Vs | Which Is Better Park Titan Or /g, '');
    contextualOverview = `
      <p>When comparing high-rise residential options in Hinjewadi, smart buyers look beyond cosmetic claims and evaluate structural density, open space continuity, and daily livability. Standalone high-rises in Hinjewadi frequently cram 10 to 14 units per lobby floor with tiny podiums, creating noisy corridors and long elevator queues.</p>
      <p><strong>Park Titan Advantage:</strong> Master-planned across 17+ acres inside the 60-acre Park District, it maintains a serene density of just 6 residences per floor with 3 high-speed elevators, an elevated 7-acre vehicle-free podium, and 5 nationally recognized sports and arts academies inside the gates.</p>
    `;
    tableRows = `
      <tr><td>Township Metric</td><td><strong>Pride Purple Park Titan</strong></td><td><strong>Standalone Hinjewadi Projects</strong></td></tr>
      <tr><td>Podium Deck</td><td><strong style="color:#d4af37">7-Acre Continuous Active Podium</strong></td><td>Fragmented 0.5 to 1.5 Acre Podiums</td></tr>
      <tr><td>Core Density</td><td><strong style="color:#d4af37">Only 6 Units Per Floor (G+23)</strong></td><td>10 to 14 Crowded Flats Per Floor</td></tr>
      <tr><td>Sports Mentorship</td><td><strong style="color:#d4af37">5 Certified National Academies</strong></td><td>Unbranded General Clubhouse Gym</td></tr>
      <tr><td>Location Access</td><td><strong style="color:#d4af37">Main Hinjewadi-Marunji Link Road</strong></td><td>Interior bypass roads with traffic jams</td></tr>
      <tr><td>Pricing Transparency</td><td><strong style="color:#d4af37">From ₹84.02L* (Verified RERA Carpet)</strong></td><td>High Loading / Super Built-Up Rates</td></tr>
    `;
  }
  // 4. Academy Slugs
  else if (slug.includes('academy') || slug.includes('padukone') || slug.includes('shiamak') || slug.includes('swim') || slug.includes('music')) {
    category = 'Professional Academies';
    entity = cleanTitle.replace(/Park Titan | Admission Fees And Coaching At Park Titan/g, '');
    contextualOverview = `
      <p>Pride Purple Park Titan is the first integrated township in Pune to embed five professional, nationally recognized sports and cultural development academies right within its gates. Families no longer spend exhausting weekend hours driving children through Hinjewadi traffic to distant academies.</p>
      <p>Resident children train under certified trainers from the Padukone School of Badminton, BSA Bluewater Swim Academy (Arjun Muralidharan), Shiamak Davar Dance Academy, SportyBeans, and Suresh Wadkar's Ajivasan Music Academy.</p>
    `;
    tableRows = `
      <tr><td>Academy Brand</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Mentorship &amp; Curriculum</td><td>National Champions &amp; Certified Legends</td></tr>
      <tr><td>Resident Privileges</td><td>Priority Batches &amp; Discounted Resident Fees</td></tr>
      <tr><td>Infrastructure</td><td>Olympic-Grade Indoor Courts &amp; Temperature Pools</td></tr>
      <tr><td>Township Setting</td><td>Pride Purple Park Titan · 17+ Acres Hinjewadi</td></tr>
    `;
  }
  // 5. NRI Slugs
  else if (slug.includes('nri') || slug.includes('investment') || slug.includes('united-states') || slug.includes('dubai') || slug.includes('singapore') || slug.includes('london')) {
    category = 'Global NRI Investment';
    entity = cleanTitle.replace(/Nri Investment Guide | Nri Investment From | In Park Titan Hinjewadi/g, '');
    contextualOverview = `
      <p>For Non-Resident Indians (NRIs) in the US, UAE, UK, Singapore, and Canada, Hinjewadi represents India's highest-yielding residential IT micro-market. Driven by 400,000+ software engineers and multinational corporate relocations, residential rental yields consistently hover at <strong>4.8% to 5.4%</strong> compared to just 3.2% in central Pune.</p>
      <p>Pride Purple provides a streamlined end-to-end digital acquisition workflow: 100% FEMA compliance, NRE/NRO fund transfers, digital token reservations, and complete rental management support.</p>
    `;
    tableRows = `
      <tr><td>NRI Target Corridor</td><td><strong>${escapeHtml(entity)}</strong></td></tr>
      <tr><td>Gross Rental Yield</td><td><strong style="color:#d4af37">4.8% – 5.4% Per Annum</strong></td></tr>
      <tr><td>5-Year Capital Appreciation</td><td><strong>9.5% – 11.2% CAGR</strong></td></tr>
      <tr><td>Compliance Standards</td><td>100% FEMA &amp; RBI Compliant</td></tr>
      <tr><td>Account Channels</td><td>NRE / NRO Direct Bank Transfer</td></tr>
      <tr><td>Starting Ticket Size</td><td>From ~₹84.02 Lakhs* ($100K USD / 370K AED)</td></tr>
    `;
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
      <tr><td>Pride Purple Project</td><td><strong>${escapeHtml(cleanTitle)}</strong></td></tr>
      <tr><td>Master Developer</td><td>Pride Purple Group (28+ Years Track Record)</td></tr>
      <tr><td>Delivered Pune Landmarks</td><td>Park Grandeur (Baner), Park Titanium (Wakad), Park Astra, Park Connect</td></tr>
      <tr><td>Township Benchmark</td><td>Park Titan · 17+ Acres, 18 Towers, 7-Acre Podium Deck</td></tr>
      <tr><td>Sanction Transparency</td><td>100% MahaRERA Sanctioned &amp; Clear Title Deeds</td></tr>
      <tr><td>Customer Desk</td><td>${PHONE_NUMBER} · ${LEAD_EMAIL}</td></tr>
    `;
  }
  // 7. Pune Real Estate Market Corridors & Benchmarks
  else if (slug.includes('hinjewadi-vs') || slug.includes('metro-line-3') || slug.includes('ring-road') || slug.includes('pune-market') || slug.includes('pune-real-estate')) {
    category = 'Pune Real Estate Market';
    entity = cleanTitle;
    contextualOverview = `
      <p>West Pune—anchored by Hinjewadi, Wakad, Baner, and Balewadi—continues to drive Maharashtra's highest residential capital appreciation and rental yield growth. Backed by 400,000+ technology professionals in Rajiv Gandhi Infotech Park, the impending operational rollout of <strong>PMRDA Metro Line 3</strong> (connecting Hinjewadi to Shivajinagar in 35 mins) and the 128 km <strong>Pune Ring Road</strong> are unlocking exponential value for gated township developments.</p>
      <p>Compared to standalone redevelopments or cramped standalone high-rises, integrated townships like <strong>Pride Purple Park Titan</strong> command 30% higher tenant preference and deliver superior long-term liquidity.</p>
    `;
    tableRows = `
      <tr><td>Market Corridor</td><td><strong>${escapeHtml(cleanTitle)}</strong></td></tr>
      <tr><td>Average Rental Yield</td><td><strong style="color:#d4af37">4.8% – 5.4%</strong> (Hinjewadi) vs 3.2% (Central Pune)</td></tr>
      <tr><td>5-Year Capital Appreciation</td><td><strong>9.5% – 11.2% CAGR</strong></td></tr>
      <tr><td>Key Transit Catalysts</td><td>Hinjewadi-Shivajinagar Metro Line 3 · 128 km Pune Ring Road</td></tr>
      <tr><td>Benchmark Development</td><td>Pride Purple Park Titan (17+ Acres, 5 Academies, 7-Acre Podium)</td></tr>
      <tr><td>Starting Sanctioned Pricing</td><td>₹84.02 Lakhs* Agreement Value (₹93.57L* All-Inclusive)</td></tr>
    `;
  }
  // Fallback / General
  else {
    entity = cleanTitle;
    contextualOverview = `
      <p>Pride Purple Park Titan Hinjewadi is an 18-tower residential landmark across 17+ prime acres on Hinjewadi-Marunji Link Road, Pune. Features 7-acre vehicle-free podium deck, 5 academies, and 40+ lifestyle amenities.</p>
    `;
    tableRows = `
      <tr><td>Project</td><td><strong>Pride Purple Park Titan</strong></td></tr>
      <tr><td>Location</td><td>Hinjewadi-Marunji Link Road, Pune</td></tr>
      <tr><td>Land Parcel</td><td>17+ Acres (60-Acre Park District)</td></tr>
      <tr><td>Configurations</td><td>2 &amp; 3 BHK Luxury Residences</td></tr>
      <tr><td>Pricing</td><td>Starting ₹84.02L* Agreement Value</td></tr>
      <tr><td>MahaRERA</td><td>${RERA_NUMBER}</td></tr>
    `;
  }

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

    <!-- 4 High Impact FAQ Accordions -->
    <div class="edge-box">
      <h2>Frequently Asked Questions</h2>
      
      <div class="faq-item">
        <div class="faq-q">What is the exact price structure and carpet area for Park Titan? <span>+</span></div>
        <div class="faq-a">2 RLK Optima (726 sq.ft.) starts at ₹84,02,750 agreement value (₹93,57,088 all-inclusive). 2 RLK Ultima (789 sq.ft.) starts at ₹90,61,500. 3 RLK formats range from 988 to 1,212 sq.ft. starting ₹1.11 Cr to ₹1.48 Cr agreement value. All-inclusive costs cover 6% stamp duty, ₹30,000 registration, and 5% GST.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Where is Park Titan located in relation to Hinjewadi Phase 1? <span>+</span></div>
        <div class="faq-a">Park Titan is situated right on the main Hinjewadi-Marunji Link Road inside the 60-acre Park District. It is only 0.8 km (2 minutes) to Wipro Circle, with upcoming Metro Line 3 station just 1 km away.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Is the project registered under MahaRERA? <span>+</span></div>
        <div class="faq-a">Yes. Pride Purple Park Titan is fully registered under multiple MahaRERA phases including P52100049631, P52100080502, P52100031768, and P52100034961. Title certificates and sanctions are verified.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">What makes the 7-acre podium deck special? <span>+</span></div>
        <div class="faq-a">The 7-acre podium deck is 100% vehicle-free. All cars and service vehicles are routed underground, creating an active, lush sanctuary where children and seniors can enjoy 40+ amenities without vehicular exhaust or hazard.</div>
      </div>
    </div>

    <!-- Related Exploration Links -->
    <div class="edge-box">
      <h2>Explore Related Corridors &amp; Configurations</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;margin-top:14px">
        <a href="/explore/2-rlk-optima-726-sqft-floor-plan-and-sanctioned-layout" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">🏢 2 BHK Optima (726 Sq.Ft.)</a>
        <a href="/explore/3-rlk-grande-1212-sqft-cost-sheet-and-price-breakdown" style="padding:10px 14px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;font-size:12px">💎 3 BHK Grande (1212 Sq.Ft.)</a>
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
    meta_desc: `Explore ${cleanTitle} at Pride Purple Park Titan Hinjewadi. 2 & 3 BHK luxury residences starting ₹84.02L*. MahaRERA ${RERA_NUMBER}. Call ${PHONE_NUMBER}.`,
    h1: cleanTitle,
    category,
    entity,
    price_val,
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
  <meta name="description" content="Explore all 10,000+ programmatic search vectors for Pride Purple Park Titan Hinjewadi: transit corridors, sanctioned 2 &amp; 3 BHK floor plans, competitor reviews, and NRI investment guides."/>
  <link rel="canonical" href="https://purpleparktitan.com/explore/"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
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
  </style>
</head>
<body>
  <div style="max-width:1300px;margin:0 auto">
    <a href="/" style="color:#d4af37;text-decoration:none;font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px">← Back to Official Home</a>
    <h1 style="margin-top:20px">Pride Purple Park Titan Exploration Hub</h1>
    <p>Welcome to the master knowledge graph for Pride Purple Park Titan Hinjewadi. Access verified engineering specifications, transit matrices to 30+ IT parks, sanctioned 2 &amp; 3 BHK floor plans, competitor audits, and global NRI investment guides.</p>

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
          <a href="/explore/2-rlk-optima-726-sqft-floor-plan-and-sanctioned-layout">2 RLK Optima (726 Sq.Ft. Carpet)</a>
          <a href="/explore/2-rlk-ultima-789-sqft-cost-sheet-and-price-breakdown">2 RLK Ultima (789 Sq.Ft. with Bay Windows)</a>
          <a href="/explore/3-rlk-optima-988-sqft-rera-carpet-area-dimensions">3 RLK Optima (988 Sq.Ft. 3 Bathrooms)</a>
          <a href="/explore/3-rlk-ultima-1060-sqft-all-inclusive-price-and-stamp-duty">3 RLK Ultima (1,060 Sq.Ft. Dual Decks)</a>
          <a href="/explore/3-rlk-grande-1212-sqft-possession-timeline-and-tower-wings">3 RLK Grande (1,212 Sq.Ft. Palatial)</a>
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
      'X-Programmatic-Hub': 'Cloudflare-Edge-Directory'
    }
  });
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}
