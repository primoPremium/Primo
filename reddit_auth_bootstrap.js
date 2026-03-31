/**
 * reddit_auth_bootstrap.js
 *
 * Run this ONCE (or whenever your session expires) to authenticate to Reddit
 * and persist the session to disk. The AI-driven browser loads from this
 * saved state and never handles credentials directly.
 *
 * Usage:
 *   REDDIT_USER=youruser REDDIT_PASS=yourpass node reddit_auth_bootstrap.js
 *
 * Or create a .env file and use dotenv (recommended).
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

// --- Config ---
const SESSION_PATH = path.resolve('./reddit_session'); // folder for browser storage
const COOKIES_PATH = path.resolve('./reddit_cookies.json'); // flat cookie export (optional)
const HEADLESS = process.env.HEADLESS !== 'false'; // set HEADLESS=false to watch it run

const REDDIT_USER = process.env.REDDIT_USER;
const REDDIT_PASS = process.env.REDDIT_PASS;

if (!REDDIT_USER || !REDDIT_PASS) {
  console.error('❌  Set REDDIT_USER and REDDIT_PASS environment variables before running.');
  process.exit(1);
}

async function bootstrap() {
  console.log('🚀  Launching browser for Reddit auth bootstrap...');

  // persistentContext saves ALL storage: cookies, localStorage, IndexedDB
  const context = await chromium.launchPersistentContext(SESSION_PATH, {
    headless: HEADLESS,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage', // important for EC2/Docker
    ],
    userAgent:
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
      '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    viewport: { width: 1280, height: 800 },
  });

  const page = await context.newPage();

  try {
    console.log('🌐  Navigating to Reddit login...');
    await page.goto('https://www.reddit.com/login/', {
      waitUntil: 'domcontentloaded',
      timeout: 30000,
    });

    // Fill username
    await page.waitForSelector('#loginUsername', { timeout: 10000 });
    await page.fill('#loginUsername', REDDIT_USER);

    // Fill password
    await page.fill('#loginPassword', REDDIT_PASS);

    // Submit
    await page.click('button[type="submit"]');

    // Wait for redirect away from login page (successful auth)
    await page.waitForURL((url) => !url.href.includes('/login'), {
      timeout: 15000,
    });

    console.log('✅  Login successful. Saving session...');

    // Export cookies separately as a flat JSON file (useful for some tools)
    const cookies = await context.cookies();
    fs.writeFileSync(COOKIES_PATH, JSON.stringify(cookies, null, 2));
    console.log(`🍪  Cookies exported to: ${COOKIES_PATH}`);

    // The persistentContext already saved everything to SESSION_PATH automatically
    console.log(`💾  Full session saved to: ${SESSION_PATH}`);

    // Quick sanity check — visit profile
    await page.goto(`https://www.reddit.com/user/${REDDIT_USER}/`, {
      waitUntil: 'domcontentloaded',
    });
    const title = await page.title();
    console.log(`🔍  Sanity check page title: "${title}"`);

    console.log('\n✅  Bootstrap complete. You can now run your AI agent with the saved session.');
  } catch (err) {
    // Check for 2FA / CAPTCHA prompt
    const url = page.url();
    if (url.includes('/login')) {
      console.error(
        '❌  Still on login page after submit. Possible causes:\n' +
        '    • Wrong credentials\n' +
        '    • Reddit CAPTCHA triggered (run with HEADLESS=false to check)\n' +
        '    • 2FA required (see note in README)'
      );
    } else {
      console.error('❌  Unexpected error:', err.message);
    }
  } finally {
    await context.close();
  }
}

bootstrap();
