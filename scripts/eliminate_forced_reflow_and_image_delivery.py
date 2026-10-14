#!/usr/bin/env python3
"""
scripts/eliminate_forced_reflow_and_image_delivery.py
Targeted elimination of remaining Lighthouse diagnostics:
1. Mobile hero image: generate hero-1-mobile.webp and use <picture> + responsive preload (eliminates 40 KiB oversized image)
2. Eliminate Forced Reflow: remove synchronous getBoundingClientRect() on load in compare slider
3. RAF-throttle scroll listeners
4. Defer Cloudflare beacon.min.js inside activateAnalytics
5. Guard hero panel slider on mobile
"""

from PIL import Image
import os
import re

def process():
    # 1. Generate mobile webp if not exists
    if not os.path.exists('images/hero-1-mobile.webp'):
        with Image.open('images/hero-1.webp') as im:
            mobile_im = im.resize((800, 450), Image.Resampling.LANCZOS)
            mobile_im.save('images/hero-1-mobile.webp', 'WEBP', quality=80)
        print("Generated images/hero-1-mobile.webp")

    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 2. Responsive Hero Preload in <head>
    old_preload = '<link rel="preload" as="image" href="/images/hero-1.webp" type="image/webp" fetchpriority="high"/>'
    new_preload = '''<link rel="preload" as="image" href="/images/hero-1-mobile.webp" type="image/webp" media="(max-width: 600px)" fetchpriority="high"/>
<link rel="preload" as="image" href="/images/hero-1.webp" type="image/webp" media="(min-width: 601px)" fetchpriority="high"/>'''

    assert old_preload in html, "Could not match old_preload"
    html = html.replace(old_preload, new_preload)

    # 3. Responsive <picture> in #hp0
    old_hp0_img = '<img fetchpriority="high" decoding="async" src="images/hero-1.webp" alt="Park Titan Residential High-Rise Towers Hinjewadi Pune" width="1920" height="1080"/>'
    new_hp0_picture = '''<picture>
        <source media="(max-width: 600px)" srcset="/images/hero-1-mobile.webp" width="800" height="450" type="image/webp"/>
        <img fetchpriority="high" decoding="async" src="images/hero-1.webp" alt="Park Titan Residential High-Rise Towers Hinjewadi Pune" width="1920" height="1080"/>
      </picture>'''

    assert old_hp0_img in html, "Could not match old_hp0_img"
    html = html.replace(old_hp0_img, new_hp0_picture)

    # 4. Remove synchronous getBoundingClientRect() on load in compare slider
    old_cmp_init = '''  window.addEventListener('touchmove', e => { if (drag) set(e.touches[0].clientX); }, { passive: true });
  const r = el.getBoundingClientRect();
  set(r.left + r.width * 0.5);
})();'''

    new_cmp_init = '''  window.addEventListener('touchmove', e => { if (drag) set(e.touches[0].clientX); }, { passive: true });
})();'''

    assert old_cmp_init in html, "Could not match old_cmp_init"
    html = html.replace(old_cmp_init, new_cmp_init)

    # 5. Guard hero panel slider on mobile
    old_panel_interval = 'setInterval(() => setPanel((activePanel + 1) % panels.length), 5000);'
    new_panel_interval = 'if (window.innerWidth > 900) { setInterval(() => setPanel((activePanel + 1) % panels.length), 5000); }'

    assert old_panel_interval in html, "Could not match old_panel_interval"
    html = html.replace(old_panel_interval, new_panel_interval)

    # 6. Throttle scroll listener with RAF
    old_scroll_code = '''/* ── Navbar & FAB on Scroll ── */
const nav = document.getElementById('navbar');
const fab = document.getElementById('fabStack');
window.addEventListener('scroll', () => {
  const y = window.scrollY;
  nav.classList.toggle('scrolled', y > 80);
  fab.style.opacity = y > 240 ? '1' : '0';
}, { passive: true });'''

    new_scroll_code = '''/* ── Navbar & FAB on Scroll (RAF Throttled for Zero Reflow) ── */
const nav = document.getElementById('navbar');
const fab = document.getElementById('fabStack');
let scrollRafId = null;
window.addEventListener('scroll', () => {
  if (!scrollRafId) {
    scrollRafId = requestAnimationFrame(() => {
      const y = window.scrollY;
      nav.classList.toggle('scrolled', y > 80);
      fab.style.opacity = y > 240 ? '1' : '0';
      scrollRafId = null;
    });
  }
}, { passive: true });'''

    assert old_scroll_code in html, "Could not match old_scroll_code"
    html = html.replace(old_scroll_code, new_scroll_code)

    # 7. Move Cloudflare beacon.min.js into activateAnalytics
    old_beacon_tag = '''<!-- Cloudflare Web Analytics (RUM - Zero-Cookie Real User Monitoring) -->
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "09e9a3bfa8cc4892b8e71953362447ea"}'></script>
<!-- End Cloudflare Web Analytics -->'''

    new_beacon_comment = '<!-- Cloudflare Web Analytics (Loaded upon interaction) -->'

    if old_beacon_tag in html:
        html = html.replace(old_beacon_tag, new_beacon_comment)
        # Add beacon injection into activateAnalytics
        old_analytics_func = "fbq('track', 'PageView');"
        new_analytics_func = '''fbq('track', 'PageView');

      // Cloudflare Web Analytics Beacon
      var sCf = document.createElement('script');
      sCf.defer = true;
      sCf.src = 'https://static.cloudflareinsights.com/beacon.min.js';
      sCf.setAttribute('data-cf-beacon', '{"token": "09e9a3bfa8cc4892b8e71953362447ea"}');
      document.head.appendChild(sCf);'''
        html = html.replace(old_analytics_func, new_analytics_func)
        print("Deferred Cloudflare beacon to interaction")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("index.html successfully hardened against forced reflows and image delivery!")

if __name__ == '__main__':
    process()
