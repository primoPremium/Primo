const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SESSION_PATH = path.resolve('./reddit_session');
const COOKIES_PATH = path.resolve('./reddit_cookies.json');

async function bootstrap() {
  if (!fs.existsSync(COOKIES_PATH)) {
    console.error('❌  reddit_cookies.json not found. Export cookies from your browser first.');
    process.exit(1);
  }

  console.log('🚀  Launching browser...');
  const context = await chromium.launchPersistentContext(SESSION_PATH, {
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    viewport: { width: 1280, height: 800 },
  });

  const page = await context.newPage();

  console.log('🍪  Injecting cookies...');
  const cookies = JSON.parse(fs.readFileSync(COOKIES_PATH, 'utf-8'));
  const cleanedCookies = cookies.map(cookie => {
  const sameSiteMap = {
    no_restriction: 'None',
    lax: 'Lax',
    strict: 'Strict',
    unspecified: 'None',
  };
  const raw = (cookie.sameSite || '').toLowerCase();
  cookie.sameSite = sameSiteMap[raw] || 'None';
  return cookie;
});
  await context.addCookies(cleanedCookies);

  console.log('🌐  Verifying session...');
  await page.goto('https://www.reddit.com/', { waitUntil: 'domcontentloaded', timeout: 20000 });

  const isLoggedIn = await page.evaluate(() => {
    return !!document.querySelector('a[href*="/user/"]');
  });

  if (isLoggedIn) {
    console.log('✅  Session verified! You are logged in.');
    console.log('💾  Session saved to ./reddit_session');
  } else {
    console.error('❌  Cookies did not work — you may not be logged in on reddit.com, or the export was incomplete.');
  }

  await context.close();
}

bootstrap();
