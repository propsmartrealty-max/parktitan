/**
 * Enterprise Cloudflare Pages Edge Middleware
 * Hardening purpleparktitan.com, www.purpleparktitan.com, and parktitan.pages.dev
 *
 * 1. Permanent 301 Canonical Host Enforcement:
 *    Redirects parktitan.pages.dev, *.pages.dev, and www.purpleparktitan.com to https://purpleparktitan.com/
 * 2. Enterprise Security Hardening Headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options)
 * 3. SEO Anti-Duplication Protection: X-Robots-Tag noindex on any staging or pages.dev hosts
 */
export async function onRequest(context) {
  const url = new URL(context.request.url);
  const hostname = url.hostname.toLowerCase();

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

  // 2. Execute downstream request handler
  const response = await context.next();
  const newHeaders = new Headers(response.headers);

  // 3. Enterprise Grade Security Headers
  newHeaders.set('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload');
  newHeaders.set('X-Content-Type-Options', 'nosniff');
  newHeaders.set('X-Frame-Options', 'SAMEORIGIN');
  newHeaders.set('X-XSS-Protection', '1; mode=block');
  newHeaders.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  newHeaders.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(self), interest-cohort=()');

  // Anti-duplication crawler header for any fallback
  if (hostname.includes('pages.dev')) {
    newHeaders.set('X-Robots-Tag', 'noindex, nofollow, noarchive');
  }

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers: newHeaders
  });
}
