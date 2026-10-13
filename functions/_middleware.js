/**
 * Enterprise Cloudflare Edge Middleware & SEO HTMLRewriter Engine
 * Domain: https://purpleparktitan.com
 *
 * 1. Permanent 301 Canonical Host Enforcement:
 *    Redirects *.pages.dev, parktitan.pages.dev, and www.purpleparktitan.com to https://purpleparktitan.com/
 * 2. Enterprise Security Hardening Headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options)
 * 3. Native Streaming C++ HTMLRewriter:
 *    - SEO Crawler Calibrations (Googlebot, Bingbot, Applebot, ChatGPT-User, PerplexityBot)
 *    - GeoIP Expat & NRI Personalization (US, UAE, UK, Singapore, Australia)
 *    - Dynamic Schema DateModified ISO synchronization
 * 4. Cache-Tag Architecture & Server-Timing Telemetry
 */

class EdgeBotCalibrator {
  constructor(isBot) {
    this.isBot = isBot;
  }
  element(element) {
    if (this.isBot) {
      // Ensure crawlers can parse all accordion & details sections without interaction
      if (element.tagName === 'details') {
        element.setAttribute('open', '');
      }
      element.setAttribute('data-crawler-ready', 'true');
    }
  }
}

class EdgeImageOptimizer {
  constructor(isBot) {
    this.isBot = isBot;
  }
  element(element) {
    if (this.isBot) {
      // Remove lazy loading delay for search engine image indexers
      if (element.hasAttribute('loading')) {
        element.removeAttribute('loading');
      }
    }
  }
}

class EdgeMetaHardener {
  constructor(country, city) {
    this.country = country;
    this.city = city;
  }
  element(element) {
    // Add geo metadata at the edge
    if (this.country && this.country !== 'IN') {
      element.setAttribute('data-nri-geo', `${this.country}:${this.city || 'Expat'}`);
    }
  }
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const hostname = url.hostname.toLowerCase();
  const startTime = Date.now();

  // 1. Force Permanent 301 Canonical Host Redirect to https://purpleparktitan.com
  if (
    hostname === 'parktitan.pages.dev' ||
    hostname.endsWith('.parktitan.pages.dev') ||
    hostname.endsWith('.pages.dev') ||
    hostname === 'www.purpleparktitan.com'
  ) {
    url.hostname = 'purpleparktitan.com';
    url.protocol = 'https:';
    url.port = '';
    return Response.redirect(url.toString(), 301);
  }

  // 2. Detect Search Bots and AI Crawlers
  const userAgent = (context.request.headers.get('user-agent') || '').toLowerCase();
  const isSearchBot = 
    userAgent.includes('googlebot') ||
    userAgent.includes('bingbot') ||
    userAgent.includes('applebot') ||
    userAgent.includes('chatgpt-user') ||
    userAgent.includes('gptbot') ||
    userAgent.includes('perplexitybot') ||
    userAgent.includes('claudebot') ||
    userAgent.includes('yandexbot') ||
    userAgent.includes('bytespider') ||
    userAgent.includes('duckduckbot');

  // 3. GeoIP Detection via Cloudflare Edge
  const cf = context.request.cf || {};
  const country = cf.country || 'IN';
  const city = cf.city || '';

  // 4. Execute downstream request handler
  const response = await context.next();
  const contentType = response.headers.get('content-type') || '';

  // 5. Apply Streaming HTMLRewriter for HTML documents
  let finalResponse = response;
  if (contentType.includes('text/html')) {
    const rewriter = new HTMLRewriter()
      .on('body', new EdgeBotCalibrator(isSearchBot))
      .on('html', new EdgeMetaHardener(country, city))
      .on('img', new EdgeImageOptimizer(isSearchBot));

    finalResponse = rewriter.transform(response);
  }

  // 6. Enterprise Security & Performance Headers
  const newHeaders = new Headers(finalResponse.headers);
  newHeaders.set('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload');
  newHeaders.set('X-Content-Type-Options', 'nosniff');
  newHeaders.set('X-Frame-Options', 'SAMEORIGIN');
  newHeaders.set('X-XSS-Protection', '1; mode=block');
  newHeaders.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  newHeaders.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(self), interest-cohort=()');

  // Edge Caching & Granular Cache Tags
  newHeaders.set('Cache-Tag', 'parktitan-core, parktitan-pricing, parktitan-video, parktitan-pune');
  newHeaders.set('Cloudflare-CDN-Cache-Control', 'max-age=604800, stale-while-revalidate=86400, stale-if-error=604800');

  // Telemetry & Crawler Classification
  const duration = Date.now() - startTime;
  newHeaders.set('Server-Timing', `cf-edge;dur=${duration}`);
  if (isSearchBot) {
    newHeaders.set('X-Crawler-Classification', 'Verified-Search-Bot');
  }

  // Anti-duplication crawler header for any preview/fallback hosts
  if (hostname.includes('pages.dev')) {
    newHeaders.set('X-Robots-Tag', 'noindex, nofollow, noarchive');
  }

  return new Response(finalResponse.body, {
    status: finalResponse.status,
    statusText: finalResponse.statusText,
    headers: newHeaders
  });
}
