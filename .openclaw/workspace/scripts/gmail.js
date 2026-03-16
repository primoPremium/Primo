const { google } = require('googleapis');
const GmailAuth = require('../auth/oauth2');

class Gmail {
  constructor(config) {
    this.auth = new GmailAuth(config);
    this.gmail = null;
  }

  async init() {
    const authClient = await this.auth.getAuthenticatedClient();
    this.gmail = google.gmail({ version: 'v1', auth: authClient });
  }

  async listMessages(options = {}) {
    if (!this.gmail) await this.init();
    
    const response = await this.gmail.users.messages.list({
      userId: 'me',
      maxResults: options.maxResults || 10,
      labelIds: options.labelIds,
      q: options.query
    });

    return response.data.messages || [];
  }

  async getMessage(messageId) {
    if (!this.gmail) await this.init();

    const response = await this.gmail.users.messages.get({
      userId: 'me',
      id: messageId,
      format: 'full'
    });

    return response.data;
  }

  async sendMessage(options) {
    if (!this.gmail) await this.init();

    const email = [
      'From: ' + options.from,
      'To: ' + options.to,
      'Subject: ' + options.subject,
      '',
      options.body
    ].join('\n');

    const encodedMessage = Buffer.from(email).toString('base64')
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=+$/, '');

    const response = await this.gmail.users.messages.send({
      userId: 'me',
      requestBody: {
        raw: encodedMessage
      }
    });

    return response.data;
  }

  async listLabels() {
    if (!this.gmail) await this.init();

    const response = await this.gmail.users.labels.list({
      userId: 'me'
    });

    return response.data.labels;
  }

  async createLabel(name) {
    if (!this.gmail) await this.init();

    const response = await this.gmail.users.labels.create({
      userId: 'me',
      requestBody: {
        name,
        labelListVisibility: 'labelShow',
        messageListVisibility: 'show'
      }
    });

    return response.data;
  }
}

module.exports = Gmail;