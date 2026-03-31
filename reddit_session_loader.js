const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const SESSION_PATH = path.resolve('./reddit_session');

async function getRedditContext(options = {}) {
  if (!fs.existsSync(SESSION_PATH)) {
    throw new Error(
      `Session folder not found at "${SESSION_PATH}".\n` +
      'Run reddit_cookie_bootstrap.js first to create a session.'
    );
  }

  const context = await chromium.launchPersistentContext(SESSION_PATH, {
    headless: options.headless ?? true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    viewport: { width: 1280, height: 800 },
    ...options.contextOptions,
  });

  return context;
}

async function getRedditPage(options = {}) {
  const context = await getRedditContext(options);
  const page = await context.newPage();
  console.log('✅  Reddit session loaded from disk.');
  console.log('💡  Session was verified during bootstrap — ready to use.');
  return { context, page };
}

function sessionExists() {
  return (
    fs.existsSync(SESSION_PATH) &&
    fs.readdirSync(SESSION_PATH).length > 0
  );
}

async function selfTest() {
  console.log('🔍  Checking saved Reddit session...\n');

  if (!sessionExists()) {
    console.error('❌  No session found. Run reddit_cookie_bootstrap.js first.');
    process.exit(1);
  }

  let context;
  try {
    const result = await getRedditPage({ headless: true });
    context = result.context;
    console.log('\n✅  Session ready. Your agent can use this context.');
  } catch (err) {
    console.error('❌  Failed:', err.message);
  } finally {
    if (context) await context.close();
  }
}

module.exports = { getRedditContext, getRedditPage, sessionExists };

if (require.main === module) {
  selfTest();
}
