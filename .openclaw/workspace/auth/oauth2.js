const { google } = require('googleapis');
const { SecureStorage } = require('@openclaw/secure-storage');
const storage = new SecureStorage();

class GmailAuth {
  constructor(config) {
    this.oauth2Client = new google.auth.OAuth2(
      config.clientId,
      config.clientSecret,
      config.redirectUri
    );
  }

  async getAuthUrl() {
    return this.oauth2Client.generateAuthUrl({
      access_type: 'offline',
      scope: [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/gmail.send',
        'https://www.googleapis.com/auth/gmail.modify'
      ]
    });
  }

  async handleCallback(code) {
    const { tokens } = await this.oauth2Client.getToken(code);
    await this.saveTokens(tokens);
    return tokens;
  }

  async refreshToken(refreshToken) {
    this.oauth2Client.setCredentials({
      refresh_token: refreshToken
    });
    const { credentials } = await this.oauth2Client.refreshAccessToken();
    await this.saveTokens(credentials);
    return credentials;
  }

  async saveTokens(tokens) {
    await storage.set('gmail_tokens', tokens);
  }

  async loadTokens() {
    return await storage.get('gmail_tokens');
  }

  async getAuthenticatedClient() {
    const tokens = await this.loadTokens();
    if (!tokens) {
      throw new Error('No tokens found. Please authenticate first.');
    }

    if (this.isTokenExpired(tokens)) {
      const newTokens = await this.refreshToken(tokens.refresh_token);
      this.oauth2Client.setCredentials(newTokens);
    } else {
      this.oauth2Client.setCredentials(tokens);
    }

    return this.oauth2Client;
  }

  isTokenExpired(tokens) {
    if (!tokens.expiry_date) return true;
    return tokens.expiry_date <= Date.now();
  }
}

module.exports = GmailAuth;