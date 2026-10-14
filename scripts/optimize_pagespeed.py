#!/usr/bin/env python3
"""
scripts/optimize_pagespeed.py
Comprehensive PageSpeed & Mobile Core Web Vitals Optimization for Pride Purple Park Titan Hinjewadi.
1. Render-blocking Google Fonts -> Preload + Async Stylesheet
2. Hero LCP image -> High-priority preload link + fetchpriority='high'
3. Deactivate blocking #loader overlay -> Instant FCP/LCP paint (< 1.2s)
4. Mobile Cursor -> Kill infinite RAF loop & touch listeners; GPU transform for desktop
5. Touch targets -> Min 48px x 48px touch bounding boxes
6. Contrast Ratios -> Boost low-alpha text to WCAG AA / AAA standards (>= 4.5:1)
7. Heading hierarchy -> Sequential descends (no h2 -> h4 skips)
8. Missing img dimensions -> Explicit width & height on all 61 images
"""

import re
import os
from bs4 import BeautifulSoup
from PIL import Image

def optimize():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Google Fonts non-render-blocking & Hero Image Preload in <head>
    # Find Google fonts link
    old_font_block = '''<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&amp;family=Bodoni+Moda:ital,opsz,wght@0,6..96,300;0,6..96,400;0,6..96,500;1,6..96,300;1,6..96,400;1,6..96,500&amp;family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&amp;family=Inter:wght@300;400;500;600&amp;family=Jost:wght@300;400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>'''

    new_font_block = '''<!-- High-Priority LCP Hero Preload & Non-Blocking Font Architecture -->
<link rel="preload" as="image" href="/images/hero-1.webp" type="image/webp" fetchpriority="high"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&amp;family=Bodoni+Moda:ital,opsz,wght@0,6..96,300;0,6..96,400;0,6..96,500;1,6..96,300;1,6..96,400;1,6..96,500&amp;family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&amp;family=Inter:wght@300;400;500;600&amp;family=Jost:wght@300;400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@300;400;500;600;700&amp;display=swap" onload="this.onload=null;this.rel='stylesheet'"/>
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&amp;family=Bodoni+Moda:ital,opsz,wght@0,6..96,300;0,6..96,400;0,6..96,500;1,6..96,300;1,6..96,400;1,6..96,500&amp;family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&amp;family=Inter:wght@300;400;500;600&amp;family=Jost:wght@300;400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@300;400;500;600;700&amp;display=swap"/>
</noscript>'''

    assert old_font_block in html, "Could not find font block in html"
    html = html.replace(old_font_block, new_font_block)

    # 2. Deactivate #loader in CSS & DOM
    old_loader_css = '''/* ── LOADER ── */
#loader {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: radial-gradient(circle at center, #1E0B20 0%, #0A040B 70%, #050206 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  transition: opacity .5s cubic-bezier(.16,1,.3,1), visibility .5s;
  pointer-events: all;
}
#loader.out {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}'''

    new_loader_css = '''/* ── LOADER (Zero-Delay Instant Render for Mobile CWV) ── */
#loader {
  display: none !important;
}
#loader.out {
  display: none !important;
}'''

    assert old_loader_css in html, "Could not find loader CSS in html"
    html = html.replace(old_loader_css, new_loader_css)

    # Also hide DOM element directly
    html = html.replace('<div id="loader" aria-label="Loading Pride Purple Park Titan">',
                        '<div id="loader" aria-label="Loading Pride Purple Park Titan" style="display:none!important">')

    # 3. Optimize Cursor CSS & JS
    old_cursor_css = '''/* ── CURSOR ── */
#cursor-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--gold);
  position: fixed;
  transform: translate(-50%,-50%);
  pointer-events: none;
  z-index: 9999;
  transition: transform .15s var(--ease1), width .3s, height .3s, opacity .3s;
}
#cursor-ring {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(200,150,60,.5);
  position: fixed;
  transform: translate(-50%,-50%);
  pointer-events: none;
  z-index: 9998;
  transition: transform .5s var(--ease1), width .3s, height .3s, border-color .3s;
}
.cursor-grow #cursor-dot {
  width: 12px;
  height: 12px;
  background: var(--gold2);
}
.cursor-grow #cursor-ring {
  width: 56px;
  height: 56px;
  border-color: var(--gold);
}'''

    new_cursor_css = '''/* ── CURSOR (Hardware-Accelerated Composited Transform) ── */
@media (hover: none) or (pointer: coarse), (max-width: 900px) {
  #cursor-dot, #cursor-ring { display: none !important; }
}
#cursor-dot {
  position: fixed;
  top: 0;
  left: 0;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--gold);
  pointer-events: none;
  z-index: 9999;
  will-change: transform;
  transform: translate3d(-100px, -100px, 0);
  transition: width .2s, height .2s, background .2s;
}
#cursor-ring {
  position: fixed;
  top: 0;
  left: 0;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(200,150,60,.5);
  pointer-events: none;
  z-index: 9998;
  will-change: transform;
  transform: translate3d(-100px, -100px, 0);
  transition: width .2s, height .2s, border-color .2s;
}
.cursor-grow #cursor-dot {
  width: 12px;
  height: 12px;
  background: var(--gold2);
}
.cursor-grow #cursor-ring {
  width: 56px;
  height: 56px;
  border-color: var(--gold);
}'''

    assert old_cursor_css in html, "Could not find cursor CSS in html"
    html = html.replace(old_cursor_css, new_cursor_css)

    # Cursor JS optimization
    old_cursor_js = '''/* ── Custom Cursor ── */
const dot = document.getElementById('cursor-dot');
const ring = document.getElementById('cursor-ring');
let mx = 0, my = 0, rx = 0, ry = 0;
document.addEventListener('mousemove', e => {
  mx = e.clientX;
  my = e.clientY;
  dot.style.left = mx + 'px';
  dot.style.top = my + 'px';
});
(function raf() {
  rx += (mx - rx) * 0.12;
  ry += (my - ry) * 0.12;
  ring.style.left = rx + 'px';
  ring.style.top = ry + 'px';
  requestAnimationFrame(raf);
})();
document.querySelectorAll('button, a, .acard, .tcard, .life-cell, .fcard, .spec-card, .fp-tab').forEach(el => {
  el.addEventListener('mouseenter', () => document.body.classList.add('cursor-grow'));
  el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-grow'));
});'''

    new_cursor_js = '''/* ── Custom Cursor (Non-Blocking, Fine-Pointer Only, RAF On-Demand) ── */
const dot = document.getElementById('cursor-dot');
const ring = document.getElementById('cursor-ring');
if (window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches && dot && ring) {
  let mx = -100, my = -100, rx = -100, ry = -100;
  let rafActive = false;
  document.addEventListener('mousemove', e => {
    mx = e.clientX;
    my = e.clientY;
    dot.style.transform = `translate3d(${mx - 4}px, ${my - 4}px, 0)`;
    if (!rafActive) {
      rafActive = true;
      requestAnimationFrame(tickRing);
    }
  }, { passive: true });
  function tickRing() {
    rx += (mx - rx) * 0.15;
    ry += (my - ry) * 0.15;
    ring.style.transform = `translate3d(${rx - 18}px, ${ry - 18}px, 0)`;
    if (Math.abs(mx - rx) > 0.1 || Math.abs(my - ry) > 0.1) {
      requestAnimationFrame(tickRing);
    } else {
      rafActive = false;
    }
  }
  document.querySelectorAll('button, a, .acard, .tcard, .life-cell, .fcard, .spec-card, .fp-tab').forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-grow'), { passive: true });
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-grow'), { passive: true });
  });
}'''

    assert old_cursor_js in html, "Could not find cursor JS in html"
    html = html.replace(old_cursor_js, new_cursor_js)

    # 4. Touch Targets: .hdot, .ap-dot, .cfg-p-btn, .fp-tab
    old_hdot_css = '''.hdot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255,255,255,.2);
  border: none;
  cursor: pointer;
  padding: 0;
  transition: all .35s;
}'''

    new_hdot_css = '''.hdot {
  position: relative;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,.5);
  border: none;
  cursor: pointer;
  padding: 0;
  transition: all .35s;
}
.hdot::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 48px;
  min-height: 48px;
}'''

    assert old_hdot_css in html, "Could not find hdot CSS in html"
    html = html.replace(old_hdot_css, new_hdot_css)

    old_apdot_css = '''.ap-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: rgba(8,8,10,.18);
  transition: all .3s;
  cursor: pointer;
}'''

    new_apdot_css = '''.ap-dot {
  position: relative;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(8,8,10,.35);
  transition: all .3s;
  cursor: pointer;
}
.ap-dot::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 48px;
  min-height: 48px;
}'''

    assert old_apdot_css in html, "Could not find apdot CSS in html"
    html = html.replace(old_apdot_css, new_apdot_css)

    old_cfg_btn_css = '''.cfg-p-btn {
  font-family: var(--f-ui);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 8px 16px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--line);
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  transition: all .25s ease;
}'''

    new_cfg_btn_css = '''.cfg-p-btn {
  font-family: var(--f-ui);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 10px 18px;
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--line);
  color: rgba(255, 255, 255, 0.85);
  cursor: pointer;
  transition: all .25s ease;
}'''

    assert old_cfg_btn_css in html, "Could not find cfg-p-btn CSS in html"
    html = html.replace(old_cfg_btn_css, new_cfg_btn_css)

    old_fptab_css = '''.fp-tab {
  font-family: var(--f-ui);
  background: rgba(8,8,10,.05);
  border: 1px solid rgba(8,8,10,.12);
  color: rgba(8,8,10,.7);
  padding: 12px 24px;
  border-radius: 40px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all .3s var(--ease1);
}'''

    new_fptab_css = '''.fp-tab {
  font-family: var(--f-ui);
  background: rgba(8,8,10,.05);
  border: 1px solid rgba(8,8,10,.18);
  color: rgba(8,8,10,.85);
  padding: 12px 24px;
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 40px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all .3s var(--ease1);
}'''

    assert old_fptab_css in html, "Could not find fp-tab CSS in html"
    html = html.replace(old_fptab_css, new_fptab_css)

    # 5. Fix Heading Hierarchy Skips
    # 5a. Mivan Section: <h4> inside .smart-spec-card -> <h3>
    html = html.replace('<h4>Monolithic Mivan RCC Structure</h4>', '<h3>Monolithic Mivan RCC Structure</h3>')
    html = html.replace('<h4>Smart Biometric Digital Locks</h4>', '<h3>Smart Biometric Digital Locks</h3>')
    html = html.replace('<h4>Color Video Door Phone (VDP)</h4>', '<h3>Color Video Door Phone (VDP)</h3>')
    html = html.replace('<h4>EV Charging Bay Infrastructure</h4>', '<h3>EV Charging Bay Infrastructure</h3>')

    # Add CSS for .smart-spec-card h3 to preserve exact visual typography
    old_spec_h4_css = '''.smart-spec-card h4 {
  font-family: var(--f-serif);
  font-size: 19px;
  color: var(--white);
  margin-bottom: 8px;
  font-weight: 400;
}'''
    new_spec_h3_css = '''.smart-spec-card h3, .smart-spec-card h4 {
  font-family: var(--f-serif);
  font-size: 19px;
  color: var(--white);
  margin-bottom: 8px;
  font-weight: 400;
}'''
    if old_spec_h4_css in html:
        html = html.replace(old_spec_h4_css, new_spec_h3_css)

    # 5b. Supremacy Cards: <h4> inside .supremacy-card -> <h3>
    html = html.replace('<h4>Reclaim 2+ Hours Daily</h4>', '<h3>Reclaim 2+ Hours Daily</h3>')
    html = html.replace('<h4>Champion Mentorship at Home</h4>', '<h3>Champion Mentorship at Home</h3>')
    html = html.replace('<h4>High-Yield Capital Appreciation</h4>', '<h3>High-Yield Capital Appreciation</h3>')

    old_sup_h4_css = '''.supremacy-card h4 {
  font-family: var(--f-serif);
  font-size: 19px;
  color: var(--white);
  margin-bottom: 8px;
  font-weight: 400;
}'''
    new_sup_h3_css = '''.supremacy-card h3, .supremacy-card h4 {
  font-family: var(--f-serif);
  font-size: 19px;
  color: var(--white);
  margin-bottom: 8px;
  font-weight: 400;
}'''
    if old_sup_h4_css in html:
        html = html.replace(old_sup_h4_css, new_sup_h3_css)

    # 5c. MahaRERA Escrow Account heading
    html = html.replace('<h4 style="font-size:16px;color:var(--white);margin:6px 0 4px">Official MahaRERA Designated Collection Account</h4>',
                        '<h3 style="font-size:16px;color:var(--white);margin:6px 0 4px">Official MahaRERA Designated Collection Account</h3>')

    # 5d. Visual Web Stories headings
    html = html.replace('<h4 style="font-family:var(--f-serif);font-size:20px;color:var(--white);line-height:1.25;margin-bottom:8px">5 Iconic Academies Inside Your Gates</h4>',
                        '<h3 style="font-family:var(--f-serif);font-size:20px;color:var(--white);line-height:1.25;margin-bottom:8px">5 Iconic Academies Inside Your Gates</h3>')
    html = html.replace('<h4 style="font-family:var(--f-serif);font-size:20px;color:var(--white);line-height:1.25;margin-bottom:8px">7-Acre Vehicle-Free Raised Podium</h4>',
                        '<h3 style="font-family:var(--f-serif);font-size:20px;color:var(--white);line-height:1.25;margin-bottom:8px">7-Acre Vehicle-Free Raised Podium</h3>')
    html = html.replace('<h4 style="font-family:var(--f-serif);font-size:20px;color:var(--white);line-height:1.25;margin-bottom:8px">2 &amp; 3 BHK Zero-Wastage Blueprints</h4>',
                        '<h3 style="font-family:var(--f-serif);font-size:20px;color:var(--white);line-height:1.25;margin-bottom:8px">2 &amp; 3 BHK Zero-Wastage Blueprints</h3>')

    # 6. Contrast Ratios: replace low alpha colors
    # Replace low alpha white text (under 0.65) with high-contrast text
    contrast_replacements = [
        ('color: rgba(255,255,255,.38);', 'color: rgba(255,255,255,.76);'),
        ('color: rgba(255,255,255,.35);', 'color: rgba(255,255,255,.76);'),
        ('color: rgba(255,255,255,.32);', 'color: rgba(255,255,255,.74);'),
        ('color: rgba(255,255,255,.28);', 'color: rgba(255,255,255,.72);'),
        ('color: rgba(255,255,255,.22);', 'color: rgba(255,255,255,.70);'),
        ('color: rgba(255,255,255,.45);', 'color: rgba(255,255,255,.82);'),
        ('color: rgba(255,255,255,.42);', 'color: rgba(255,255,255,.80);'),
        ('color: rgba(255,255,255,.48);', 'color: rgba(255,255,255,.82);'),
        ('color: rgba(255,255,255,.5);',  'color: rgba(255,255,255,.82);'),
        ('color: rgba(255,255,255,.55);', 'color: rgba(255,255,255,.85);'),
        ('color: rgba(255,255,255, 0.35);', 'color: rgba(255,255,255, 0.76);'),
        ('color: rgba(255,255,255, 0.45);', 'color: rgba(255,255,255, 0.82);'),
        ('color: rgba(255,255,255, 0.5);',  'color: rgba(255,255,255, 0.82);'),
        ('color:rgba(255,255,255,0.5)',     'color:rgba(255,255,255,0.82)'),
        ('color:rgba(255,255,255,.45)',     'color:rgba(255,255,255,.82)'),
        ('color:rgba(255,255,255,.4)',      'color:rgba(255,255,255,.80)'),
        ('color:rgba(255,255,255,.5)',      'color:rgba(255,255,255,.82)'),
        ('color:rgba(255,255,255,.28)',     'color:rgba(255,255,255,.72)'),
        ('color:rgba(255,255,255,.2)',      'color:rgba(255,255,255,.70)'),
        # Dark text on light backgrounds
        ('color: rgba(8,8,10,.5);',  'color: rgba(8,8,10,.82);'),
        ('color: rgba(8,8,10,.4);',  'color: rgba(8,8,10,.80);'),
        ('color: rgba(8,8,10,.6);',  'color: rgba(8,8,10,.84);'),
        ('color: rgba(8,8,10,.62);', 'color: rgba(8,8,10,.85);'),
        ('color: rgba(8,8,10,.7);',  'color: rgba(8,8,10,.88);'),
    ]

    for old_c, new_c in contrast_replacements:
        html = html.replace(old_c, new_c)

    # 7. Add explicit width and height, loading="lazy", and decoding="async" to all <img> tags
    # Parse HTML with BeautifulSoup and update img tags directly or via string replacement
    # Let's inspect local files and build dimensions dictionary
    img_dims = {
        'images/purple-emblem.png': (256, 256),
        '/images/purple-emblem.png': (256, 256),
        'images/logo-park-titan.png': (260, 179),
        '/images/logo-park-titan.png': (260, 179),
        'images/hero-1.webp': (1920, 1080),
        '/images/hero-1.webp': (1920, 1080),
        'images/moment-leisure.webp': (1000, 558),
        '/images/moment-leisure.webp': (1000, 558),
        'images/moment-wellness.webp': (1000, 1000),
        '/images/moment-wellness.webp': (1000, 1000),
        'images/moment-sports.webp': (1000, 1000),
        '/images/moment-sports.webp': (1000, 1000),
        'images/moment-kids.webp': (1000, 558),
        '/images/moment-kids.webp': (1000, 558),
        'images/moment-community.webp': (1000, 1000),
        '/images/moment-community.webp': (1000, 1000),
        'images/park-life.webp': (1600, 912),
        '/images/park-life.webp': (1600, 912),
        'images/traffic.webp': (1600, 912),
        '/images/traffic.webp': (1600, 912),
        'images/cat-it.webp': (1400, 1400),
        '/images/cat-it.webp': (1400, 1400),
        'images/cat-education.webp': (1400, 1400),
        '/images/cat-education.webp': (1400, 1400),
        'images/cat-healthcare.webp': (1400, 1400),
        '/images/cat-healthcare.webp': (1400, 1400),
        'images/cat-shopping.webp': (1400, 1400),
        '/images/cat-shopping.webp': (1400, 1400),
        'images/cat-connectivity.webp': (1400, 1400),
        '/images/cat-connectivity.webp': (1400, 1400),
        'images/cat-dining.webp': (1400, 1400),
        '/images/cat-dining.webp': (1400, 1400),
        'images/academy-badminton.webp': (1400, 781),
        '/images/academy-badminton.webp': (1400, 781),
        'images/logo-badminton.png': (100, 100),
        '/images/logo-badminton.png': (100, 100),
        'images/academy-swimming.webp': (1400, 781),
        '/images/academy-swimming.webp': (1400, 781),
        'images/logo-swimming.png': (100, 100),
        '/images/logo-swimming.png': (100, 100),
        'images/academy-dance.webp': (1400, 786),
        '/images/academy-dance.webp': (1400, 786),
        'images/logo-dance.png': (100, 100),
        '/images/logo-dance.png': (100, 100),
        'images/academy-sports.webp': (1400, 781),
        '/images/academy-sports.webp': (1400, 781),
        'images/logo-sports.png': (100, 100),
        '/images/logo-sports.png': (100, 100),
        'images/academy-music.webp': (1400, 781),
        '/images/academy-music.webp': (1400, 781),
        'images/logo-music.png': (100, 100),
        '/images/logo-music.png': (100, 100),
        'images/plans/master-plan.jpeg': (1280, 905),
        '/images/plans/master-plan.jpeg': (1280, 905),
        'images/plans/floor-plan-2bhk.jpeg': (1280, 905),
        '/images/plans/floor-plan-2bhk.jpeg': (1280, 905),
        'images/plans/floor-plan-3bhk.jpeg': (1280, 905),
        '/images/plans/floor-plan-3bhk.jpeg': (1280, 905),
        'images/config-2bhk.webp': (1800, 1202),
        '/images/config-2bhk.webp': (1800, 1202),
        'images/config-3bhk-a.webp': (646, 630),
        '/images/config-3bhk-a.webp': (646, 630),
        'images/config-3bhk-b.webp': (1800, 1202),
        '/images/config-3bhk-b.webp': (1800, 1202),
        'images/config-3bhk-c.webp': (616, 618),
        '/images/config-3bhk-c.webp': (616, 618),
        'images/logos/purple-corp.webp': (260, 78),
        '/images/logos/purple-corp.webp': (260, 78),
        'images/logos/titan.webp': (800, 300),
        '/images/logos/titan.webp': (800, 300),
        'images/logos/astra.webp': (800, 300),
        '/images/logos/astra.webp': (800, 300),
        'images/logos/landmark.webp': (800, 300),
        '/images/logos/landmark.webp': (800, 300),
        'images/logos/connect.webp': (800, 300),
        '/images/logos/connect.webp': (800, 300),
        'images/logos/plaza.webp': (800, 300),
        '/images/logos/plaza.webp': (800, 300),
        'images/logos/pride-purple-square.webp': (800, 300),
        '/images/logos/pride-purple-square.webp': (800, 300),
        'images/logos/titanium.webp': (800, 300),
        '/images/logos/titanium.webp': (800, 300),
        'images/logos/grandeur.webp': (800, 300),
        '/images/logos/grandeur.webp': (800, 300),
        'images/logos/xpress.webp': (800, 300),
        '/images/logos/xpress.webp': (800, 300),
        'images/logos/ivory.webp': (800, 300),
        '/images/logos/ivory.webp': (800, 300),
        'images/logos/eden.png': (226, 66),
        '/images/logos/eden.png': (226, 66),
        'images/logos/pebbles.png': (228, 150),
        '/images/logos/pebbles.png': (228, 150),
        'images/locality-hinjawadi.webp': (1400, 1400),
        '/images/locality-hinjawadi.webp': (1400, 1400),
        'images/qr_502.png': (340, 340),
        '/images/qr_502.png': (340, 340),
        'images/qr1.webp': (150, 150),
        '/images/qr1.webp': (150, 150),
        'https://img.youtube.com/vi/ofkenFQHvEU/maxresdefault.jpg': (1280, 720),
        'https://img.youtube.com/vi/pZKpUTM1P88/maxresdefault.jpg': (1280, 720),
    }

    # Replace <img> tags with proper width, height, decoding="async" and loading="lazy" (hero gets fetchpriority="high")
    def img_replacer(match):
        tag = match.group(0)
        # Extract src
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
        if not src_m:
            return tag
        src = src_m.group(1)

        dims = img_dims.get(src)
        if not dims:
            clean = src.lstrip('/')
            dims = img_dims.get(clean)

        new_tag = tag

        # Add decoding="async" if not present
        if 'decoding=' not in new_tag:
            new_tag = new_tag.replace('<img ', '<img decoding="async" ')

        # Handle width and height
        if dims:
            w, h = dims
            if 'width=' not in new_tag:
                new_tag = new_tag.replace('<img ', f'<img width="{w}" ')
            if 'height=' not in new_tag:
                new_tag = new_tag.replace('<img ', f'<img height="{h}" ')

        # If hero image, ensure fetchpriority="high" and no lazy
        if 'hero-1.webp' in src:
            new_tag = re.sub(r'\s*loading=["\']lazy["\']', '', new_tag)
            if 'fetchpriority=' not in new_tag:
                new_tag = new_tag.replace('<img ', '<img fetchpriority="high" ')
        else:
            # Below the fold: ensure loading="lazy" if not present and not in hero
            if 'loading=' not in new_tag and 'purple-emblem' not in src and 'logo-park-titan' not in src:
                new_tag = new_tag.replace('<img ', '<img loading="lazy" ')

        return new_tag

    html = re.sub(r'<img\s+[^>]+>', img_replacer, html)

    # 8. Check hero panel 0 image tag specifically
    html = html.replace('<img src="images/hero-1.webp" alt="Park Titan Residential High-Rise Towers Hinjewadi Pune" width="1920" height="1080"/>',
                        '<img src="images/hero-1.webp" alt="Park Titan Residential High-Rise Towers Hinjewadi Pune" width="1920" height="1080" fetchpriority="high" decoding="async"/>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("index.html optimization successfully applied!")

if __name__ == '__main__':
    optimize()
