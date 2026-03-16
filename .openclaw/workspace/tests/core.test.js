const { expect } = require('chai');
const sinon = require('sinon');
const Gmail = require('../scripts/gmail');
const GmailAuth = require('../auth/oauth2');

describe('Gmail Skill Tests', () => {
  let gmail;
  let auth;
  const config = {
    clientId: 'test-client-id',
    clientSecret: 'test-client-secret',
    redirectUri: 'http://localhost:3000/oauth2callback'
  };

  beforeEach(() => {
    auth = new GmailAuth(config);
    gmail = new Gmail(config);
  });

  describe('Authentication', () => {
    it('should generate auth URL with correct scopes', async () => {
      const url = await auth.getAuthUrl();
      expect(url).to.include('gmail.readonly');
      expect(url).to.include('gmail.send');
      expect(url).to.include('gmail.modify');
    });

    it('should handle OAuth2 callback', async () => {
      const code = 'test-auth-code';
      const mockTokens = {
        access_token: 'test-access-token',
        refresh_token: 'test-refresh-token',
        expiry_date: Date.now() + 3600000
      };

      sinon.stub(auth.oauth2Client, 'getToken').resolves({ tokens: mockTokens });
      sinon.stub(auth, 'saveTokens').resolves();

      const tokens = await auth.handleCallback(code);
      expect(tokens).to.deep.equal(mockTokens);
    });
  });

  describe('Email Operations', () => {
    beforeEach(() => {
      sinon.stub(auth, 'getAuthenticatedClient').resolves(auth.oauth2Client);
    });

    it('should list messages', async () => {
      const mockMessages = [
        { id: '1', threadId: 'thread1' },
        { id: '2', threadId: 'thread2' }
      ];

      sinon.stub(gmail.gmail.users.messages, 'list')
        .resolves({ data: { messages: mockMessages } });

      const messages = await gmail.listMessages();
      expect(messages).to.deep.equal(mockMessages);
    });

    it('should send message', async () => {
      const messageOptions = {
        to: 'test@example.com',
        subject: 'Test',
        body: 'Test message'
      };

      sinon.stub(gmail.gmail.users.messages, 'send')
        .resolves({ data: { id: 'sent-message-id' } });

      const result = await gmail.sendMessage(messageOptions);
      expect(result.id).to.equal('sent-message-id');
    });
  });
});