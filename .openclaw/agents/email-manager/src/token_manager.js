const { SecureStorage } = require('@openclaw/secure-storage');
const storage = new SecureStorage();

async function saveTokens(tokens) {
  await storage.set('gmail_tokens', tokens);
  console.log('Tokens saved successfully');
}

async function loadTokens() {
  const tokens = await storage.get('gmail_tokens');
  console.log('Tokens loaded successfully');
  return tokens;
}

module.exports = {
  saveTokens,
  loadTokens
};