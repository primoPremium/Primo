const { google } = require('googleapis');
const fs = require('fs').promises;
const path = require('path');
const config = require('config');

class GmailAuth {
  constructor() {
    this.oauth2Client = new google.auth.OAuth2(
      config.get('gmail.clientId'),
      config.get('gmail.clientSecret'),
      config.get('gmail.redirectUri')
    );
    
    this.SCOPES = [
      'https://www.googleapis.com/auth/gmail.modify',
      'https://www.googleapis.com/auth/gmail.compose',
      'https://www.googleapis.com/auth/gmail.labels'
    ];
  }

  async getAuthUrl() {
    return this.oauth2Client.generateAuthUrl({
      access_type: 'offline',
      scope: this.SCOPES,
      prompt: 'consent'
    });
  }

  async getTokens(code) {
    const { tokens } = await this.oauth2Client.getToken(code);
    await this.saveTokens(tokens);
    return tokens;
  }

  async saveTokens(tokens) {
    const tokenPath = path.join(process.env.HOME, '.openclaw', 'credentials', 'gmail-tokens.json');
    await fs.writeFile(tokenPath, JSON.stringify(tokens));
  }

  async loadTokens() {
    try {
      const tokenPath = path.join(process.env.HOME, '.openclaw', 'credentials', 'gmail-tokens.json');
      const tokens = JSON.parse(await fs.readFile(tokenPath));
      this.oauth2Client.setCredentials(tokens);
      return tokens;
    } catch (error) {
      throw new Error('No tokens found - authentication required');
    }
  }

  async refreshTokens() {
    try {
      const { credentials } = await this.oauth2Client.refreshAccessToken();
      await this.saveTokens(credentials);
      return credentials;
    } catch (error) {
      throw new Error('Failed to refresh tokens: ' + error.message);
    }
  }

  getAuthenticatedClient() {
    return google.gmail({ version: 'v1', auth: this.oauth2Client });
  }

  async validateTokens() {
    try {
      const tokens = await this.loadTokens();
      if (this.isTokenExpired(tokens)) {
        return await this.refreshTokens();
      }
      return tokens;
    } catch (error) {
      throw new Error('Token validation failed: ' + error.message);
    }
  }

  isTokenExpired(tokens) {
    const expiryDate = tokens.expiry_date;
    return expiryDate ? expiryDate <= Date.now() : true;
  }
}

module.exports = new GmailAuth();