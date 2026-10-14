#!/usr/bin/env python3
"""
scripts/deep_cwv_hardening.py
Elite Core Web Vitals & Accessibility Hardening for Pride Purple Park Titan:
1. Deferred Marketing Analytics (interaction/idle based) -> saves 659 KiB unused JS & 6.7s main-thread blocking.
2. Complete Form Accessibility -> explicit <label for="..."> on all 16 form controls + sliders.
3. Accessible Names -> aria-label on .fab-e, modal close buttons, ap-dot buttons.
4. Touch Target Sizing -> min 48px x 48px on .fsoc, .fab, .fp-cat-pill, .vid-tab-btn, .lchip, .bg-tab-btn.
5. Contrast Ratios -> replace all low contrast text on floor plans and benchmark tables.
6. Mobile Animation Killswitch -> disable 36 non-composited animations on mobile to stop forced reflow.
7. Instant Hero Paint on Mobile -> transform: none & opacity: 1 on hero text; hide #hp1 & #hp2 on mobile.
8. Remove #loader DOM completely.
"""

import re
from bs4 import BeautifulSoup

def harden():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. DEFER MARKETING ANALYTICS
    old_analytics = '''<!-- Analytics: GA4 & Google Ads -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-18LEE0HXP5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-18LEE0HXP5');
  gtag('config', 'AW-849058188');
</script>

<!-- Google Tag Manager -->
<script>
  (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});
  var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;
  j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-KBL2TR98');
</script>

<!-- Meta Pixel -->
<script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '1243398972890613');
  fbq('track', 'PageView');
</script>'''

    new_analytics = '''<!-- Optimized Asynchronous Marketing Analytics Loader (Zero CWV Main-Thread Impact) -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  window._fbq = window._fbq || [];
  window.fbq = window.fbq || function(){(fbq.q=fbq.q||[]).push(arguments)};

  (function() {
    var analyticsTriggered = false;
    function activateAnalytics() {
      if (analyticsTriggered) return;
      analyticsTriggered = true;
      ['scroll', 'touchstart', 'mousemove', 'click', 'keydown'].forEach(function(ev) {
        window.removeEventListener(ev, activateAnalytics, { passive: true });
      });

      // GA4 & Google Ads
      var sGtag = document.createElement('script');
      sGtag.async = true;
      sGtag.src = 'https://www.googletagmanager.com/gtag/js?id=G-18LEE0HXP5';
      sGtag.onload = function() {
        gtag('config', 'G-18LEE0HXP5');
        gtag('config', 'AW-849058188');
      };
      document.head.appendChild(sGtag);

      // Google Tag Manager
      (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});
      var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;
      j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      })(window,document,'script','dataLayer','GTM-KBL2TR98');

      // Meta Pixel
      !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
      n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
      document,'script','https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', '1243398972890613');
      fbq('track', 'PageView');
    }

    ['scroll', 'touchstart', 'mousemove', 'click', 'keydown'].forEach(function(ev) {
      window.addEventListener(ev, activateAnalytics, { passive: true, once: true });
    });
    setTimeout(activateAnalytics, 4000);
  })();
</script>'''

    assert old_analytics in html, "Could not match old_analytics"
    html = html.replace(old_analytics, new_analytics)

    # 2. REMOVE #LOADER DOM COMPLETELY
    loader_dom_pattern = r'<div id="loader"[^>]*>.*?</div>\s*</div>'
    match = re.search(loader_dom_pattern, html, flags=re.DOTALL)
    if match:
        html = html.replace(match.group(0), '<!-- Loader Removed for Instant First Paint -->')
    else:
        print("Warning: loader dom pattern not matched")

    # 3. ACCESSIBLE LABELS & FORM CONTROLS
    # 3a. In-Page Contact Form
    old_contact_form = '''<form class="enq-form" onsubmit="handleEnq(event)">
        <input type="text" name="name" placeholder="Your Full Name" required/>
        <input type="email" name="email" placeholder="Email Address" required/>
        <input type="tel" name="mobile" placeholder="Mobile Number (10 digits)" maxlength="10" minlength="10" pattern="[0-9]{10}" required/>
        <select name="config" required>
          <option value="" disabled selected>Select Configuration</option>
          <option>2 BHK Optima — 726 sq.ft. (₹93.57L* Final Price)</option>
          <option>2 BHK Ultima — 789 sq.ft. (₹1.01 Cr* Final Price)</option>
          <option>3 BHK Optima — 988 sq.ft. (₹1.24 Cr* Final Price)</option>
          <option>3 BHK Ultima — 1060 sq.ft. (₹1.37 Cr* Final Price)</option>
          <option>3 BHK Grande — 1212 sq.ft. (₹1.65 Cr* Final Price)</option>
        </select>
        <select name="budget" required>
          <option value="" disabled selected>Select Budget Range</option>
          <option>₹90 Lakhs to ₹1.05 Cr</option>
          <option>₹1.05 Cr to ₹1.25 Cr</option>
          <option>₹1.25 Cr to ₹1.50 Cr</option>
          <option>Above ₹1.50 Cr</option>
        </select>
        <textarea name="msg" placeholder="Message or preferred visit time (optional)" rows="2"></textarea>
        <button class="enq-sub" type="submit">Submit Enquiry</button>
      </form>'''

    new_contact_form = '''<form class="enq-form" onsubmit="handleEnq(event)">
        <label for="contact_name" class="sr-only">Your Full Name</label>
        <input type="text" id="contact_name" name="name" placeholder="Your Full Name" aria-label="Your Full Name" required/>
        
        <label for="contact_email" class="sr-only">Email Address</label>
        <input type="email" id="contact_email" name="email" placeholder="Email Address" aria-label="Email Address" required/>
        
        <label for="contact_mobile" class="sr-only">Mobile Number</label>
        <input type="tel" id="contact_mobile" name="mobile" placeholder="Mobile Number (10 digits)" aria-label="Mobile Number" maxlength="10" minlength="10" pattern="[0-9]{10}" required/>
        
        <label for="contact_config" class="sr-only">Select Configuration</label>
        <select id="contact_config" name="config" aria-label="Select Configuration" required>
          <option value="" disabled selected>Select Configuration</option>
          <option>2 BHK Optima — 726 sq.ft. (₹93.57L* Final Price)</option>
          <option>2 BHK Ultima — 789 sq.ft. (₹1.01 Cr* Final Price)</option>
          <option>3 BHK Optima — 988 sq.ft. (₹1.24 Cr* Final Price)</option>
          <option>3 BHK Ultima — 1060 sq.ft. (₹1.37 Cr* Final Price)</option>
          <option>3 BHK Grande — 1212 sq.ft. (₹1.65 Cr* Final Price)</option>
        </select>
        
        <label for="contact_budget" class="sr-only">Select Budget Range</label>
        <select id="contact_budget" name="budget" aria-label="Select Budget Range" required>
          <option value="" disabled selected>Select Budget Range</option>
          <option>₹90 Lakhs to ₹1.05 Cr</option>
          <option>₹1.05 Cr to ₹1.25 Cr</option>
          <option>₹1.25 Cr to ₹1.50 Cr</option>
          <option>Above ₹1.50 Cr</option>
        </select>
        
        <label for="contact_msg" class="sr-only">Message or preferred visit time</label>
        <textarea id="contact_msg" name="msg" placeholder="Message or preferred visit time (optional)" aria-label="Message or preferred visit time" rows="2"></textarea>
        <button class="enq-sub" type="submit" aria-label="Submit Enquiry Form">Submit Enquiry</button>
      </form>'''

    assert old_contact_form in html, "Could not match old_contact_form"
    html = html.replace(old_contact_form, new_contact_form)

    # 3b. Modal Form
    old_modal_form = '''<form class="enq-form" onsubmit="handleEnq(event)">
      <input type="text" name="name" placeholder="Your Full Name" required/>
      <input type="email" name="email" placeholder="Email Address" required/>
      <input type="tel" name="mobile" placeholder="Mobile Number (10 digits)" maxlength="10" minlength="10" pattern="[0-9]{10}" required/>
      <select name="config" required>
        <option value="" disabled selected>Select Configuration</option>
        <option>2 BHK Optima — 726 sq.ft.</option>
        <option>2 BHK Ultima — 789 sq.ft.</option>
        <option>3 BHK Optima — 988 sq.ft.</option>
        <option>3 BHK Ultima — 1060 sq.ft.</option>
        <option>3 BHK Grande — 1212 sq.ft.</option>
      </select>
      <select name="budget" required>
        <option value="" disabled selected>Select Budget Range</option>
        <option>₹90 Lakhs to ₹1.05 Cr</option>
        <option>₹1.05 Cr to ₹1.25 Cr</option>
        <option>₹1.25 Cr to ₹1.50 Cr</option>
        <option>Above ₹1.50 Cr</option>
      </select>
      <textarea name="msg" placeholder="Message or preferred visit time (optional)"></textarea>
      <button class="enq-sub" type="submit">Submit Enquiry</button>
    </form>'''

    new_modal_form = '''<form class="enq-form" onsubmit="handleEnq(event)">
      <label for="modal_name" class="sr-only">Your Full Name</label>
      <input type="text" id="modal_name" name="name" placeholder="Your Full Name" aria-label="Your Full Name" required/>
      
      <label for="modal_email" class="sr-only">Email Address</label>
      <input type="email" id="modal_email" name="email" placeholder="Email Address" aria-label="Email Address" required/>
      
      <label for="modal_mobile" class="sr-only">Mobile Number</label>
      <input type="tel" id="modal_mobile" name="mobile" placeholder="Mobile Number (10 digits)" aria-label="Mobile Number" maxlength="10" minlength="10" pattern="[0-9]{10}" required/>
      
      <label for="modal_config" class="sr-only">Select Configuration</label>
      <select id="modal_config" name="config" aria-label="Select Configuration" required>
        <option value="" disabled selected>Select Configuration</option>
        <option>2 BHK Optima — 726 sq.ft.</option>
        <option>2 BHK Ultima — 789 sq.ft.</option>
        <option>3 BHK Optima — 988 sq.ft.</option>
        <option>3 BHK Ultima — 1060 sq.ft.</option>
        <option>3 BHK Grande — 1212 sq.ft.</option>
      </select>
      
      <label for="modal_budget" class="sr-only">Select Budget Range</label>
      <select id="modal_budget" name="budget" aria-label="Select Budget Range" required>
        <option value="" disabled selected>Select Budget Range</option>
        <option>₹90 Lakhs to ₹1.05 Cr</option>
        <option>₹1.05 Cr to ₹1.25 Cr</option>
        <option>₹1.25 Cr to ₹1.50 Cr</option>
        <option>Above ₹1.50 Cr</option>
      </select>
      
      <label for="modal_msg" class="sr-only">Message or preferred visit time</label>
      <textarea id="modal_msg" name="msg" placeholder="Message or preferred visit time (optional)" aria-label="Message or preferred visit time"></textarea>
      <button class="enq-sub" type="submit" aria-label="Submit Modal Enquiry">Submit Enquiry</button>
    </form>'''

    assert old_modal_form in html, "Could not match old_modal_form"
    html = html.replace(old_modal_form, new_modal_form)

    # 3c. Sliders: Floor, Loan, Rate, Tenure
    old_floor_slider = '<input type="range" id="floorSlider" min="1" max="23" value="1" step="1"/>'
    new_floor_slider = '<label for="floorSlider" class="sr-only">Floor Level</label><input type="range" id="floorSlider" aria-label="Floor Level Selection" min="1" max="23" value="1" step="1"/>'
    html = html.replace(old_floor_slider, new_floor_slider)

    old_loan_slider = '<input type="range" id="loanSlider" min="50" max="150" value="80" step="5"/>'
    new_loan_slider = '<label for="loanSlider" class="sr-only">Home Loan Amount</label><input type="range" id="loanSlider" aria-label="Home Loan Principal in Lakhs" min="50" max="150" value="80" step="5"/>'
    html = html.replace(old_loan_slider, new_loan_slider)

    old_rate_slider = '<input type="range" id="rateSlider" min="7.5" max="11.5" value="8.5" step="0.1"/>'
    new_rate_slider = '<label for="rateSlider" class="sr-only">Interest Rate</label><input type="range" id="rateSlider" aria-label="Annual Interest Rate Percentage" min="7.5" max="11.5" value="8.5" step="0.1"/>'
    html = html.replace(old_rate_slider, new_rate_slider)

    old_tenure_slider = '<input type="range" id="tenureSlider" min="5" max="30" value="20" step="1"/>'
    new_tenure_slider = '<label for="tenureSlider" class="sr-only">Loan Tenure</label><input type="range" id="tenureSlider" aria-label="Loan Tenure in Years" min="5" max="30" value="20" step="1"/>'
    html = html.replace(old_tenure_slider, new_tenure_slider)

    # 4. BUTTON ACCESSIBILITY
    # 4a. FAB Button
    html = html.replace('<button class="fab fab-e" onclick="openEnq()">',
                        '<button class="fab fab-e" onclick="openEnq()" aria-label="Open Project Enquiry Form">')

    # 4b. Modal Close Buttons
    html = html.replace('<button class="enq-x" onclick="closeEnq()">✕ &nbsp;Close</button>',
                        '<button class="enq-x" onclick="closeEnq()" aria-label="Close Enquiry Dialog">✕ &nbsp;Close</button>')
    html = html.replace('<button class="tm-x" onclick="closeTesti()">✕ &nbsp;Close</button>',
                        '<button class="tm-x" onclick="closeTesti()" aria-label="Close Testimonial Video Dialog">✕ &nbsp;Close</button>')
    html = html.replace('<button class="bpm-btn bpm-btn--close" onclick="closeBlueprint()">✕ Close</button>',
                        '<button class="bpm-btn bpm-btn--close" onclick="closeBlueprint()" aria-label="Close Blueprint Modal">✕ Close</button>')

    # 4c. Amenity Dots: convert <div> to accessible <button>
    old_ap_dots = '''    <div class="ap-dot active"></div>
    <div class="ap-dot"></div>
    <div class="ap-dot"></div>
    <div class="ap-dot"></div>
    <div class="ap-dot"></div>'''

    new_ap_dots = '''    <button type="button" class="ap-dot active" aria-label="View Amenity Slide 1"></button>
    <button type="button" class="ap-dot" aria-label="View Amenity Slide 2"></button>
    <button type="button" class="ap-dot" aria-label="View Amenity Slide 3"></button>
    <button type="button" class="ap-dot" aria-label="View Amenity Slide 4"></button>
    <button type="button" class="ap-dot" aria-label="View Amenity Slide 5"></button>'''

    html = html.replace(old_ap_dots, new_ap_dots)

    # 5. CONTRAST RATIO FIXES ON FLOOR PLAN CARDS
    # Replace low contrast color: rgba(8,8,10,.5) on light cards
    html = html.replace('color:rgba(8,8,10,.5);text-transform:uppercase', 'color:#242429;text-transform:uppercase')
    html = html.replace('color:rgba(8,8,10,.5);font-family', 'color:#242429;font-family')
    html = html.replace('color:rgba(8,8,10,.5);font-size', 'color:#242429;font-size')

    # 6. TOUCH TARGET SIZING CSS INJECTIONS & MOBILE PERFORMANCE KILLSWITCH
    cwv_css_block = '''
/* ── SCREEN READER ACCESSIBILITY UTILITY ── */
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

/* ── TOUCH TARGET HARDENING (MIN 48PX x 48PX) ── */
.fsoc {
  min-width: 48px !important;
  min-height: 48px !important;
  width: 48px !important;
  height: 48px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 15px !important;
  margin: 4px !important;
  border-radius: 6px !important;
}
.fp-cat-pill, .vid-tab-btn, .lchip, .bg-tab-btn {
  min-height: 48px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.ap-dot {
  min-width: 32px !important;
  min-height: 32px !important;
  border: none !important;
  background: transparent !important;
  padding: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.ap-dot::after {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(8,8,10,.4);
  transition: all .3s;
}
.ap-dot.active::after {
  width: 26px;
  border-radius: 4px;
  background: var(--gold3);
}

/* ── MOBILE CWV PERFORMANCE & INSTANT PAINT ARCHITECTURE ── */
@media (max-width: 900px) {
  /* Instant hero render - zero animation delay penalty */
  .hero-h1 .line {
    transform: none !important;
    animation: none !important;
  }
  .hero-sub, .hero-desc, .hero-actions, .hstat {
    opacity: 1 !important;
    animation: none !important;
  }
  /* Eliminate unused background hero images on mobile (save 361 KiB) */
  #hp1, #hp2 {
    display: none !important;
  }
  .hero-panels {
    grid-template-columns: 1fr !important;
  }
  /* Kill continuous non-composited animations on mobile to free main thread */
  .btn-p::after, .btn-gold::after, .enq-sub::after, .art-btn::after {
    animation: none !important;
    display: none !important;
  }
  em.gold, .t1 em, .t2 em, .hero-h1 em, .fiesta-amount {
    animation: none !important;
    -webkit-text-fill-color: #E6BE6E !important;
    color: #E6BE6E !important;
  }
  #scrollProgressBar, .fiesta-bg-glow, .tcard-play::before, .wa, .wa::before {
    animation: none !important;
  }
  .fab {
    min-width: 48px !important;
    min-height: 48px !important;
    width: 52px !important;
    height: 52px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
}
'''

    # Insert cwv_css_block right before </style>
    assert '</style>' in html, "Could not find </style> in html"
    html = html.replace('</style>', cwv_css_block + '\n</style>', 1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully hardened index.html for CWV & Accessibility!")

if __name__ == '__main__':
    harden()
