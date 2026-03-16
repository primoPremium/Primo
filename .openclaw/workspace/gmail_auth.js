const {google} = require('googleapis');
const fs = require('fs').promises;
const path = require('path');
const express = require('express');
const open = require('open');

// OAuth 2.0 configuration
const CLIENT_ID = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const REDIRECT_URI = 'http://localhost:3000/oauth2callback';
const SCOPES = ['https://www.googleapis.com/auth/gmail.send'];

const oauth2Client = new google.auth.OAuth2(
  CLIENT_ID,
  CLIENT_SECRET,
  REDIRECT_URI
);

async function getAccessToken() {
  const app = express();
  let server;
  
  return new Promise((resolve, reject) => {
    app.get('/oauth2callback', async (req, res) => {
      try {
        const {code} = req.query;
        const {tokens} = await oauth2Client.getToken(code);
        await fs.writeFile('gmail_tokens.json', JSON.stringify(tokens, null, 2));
        res.send('Authorization successful! You can close this window.');
        server.close();
        resolve(tokens);
      } catch (err) {
        reject(err);
      }
    });

    server = app.listen(3000, async () => {
      const authUrl = oauth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
      });
      console.log('Please visit this URL to authorize the application:', authUrl);
      await open(authUrl);
    });
  });
}

// Test sending email
async function sendTestEmail(auth) {
  const gmail = google.gmail({version: 'v1', auth});
  const email = [
    'From: "Test Sender" <me@example.com>',
    'To: me@example.com',
    'Subject: Test Email',
    '',
    'This is a test email sent using Gmail API.',
  ].join('\n');

  const encodedEmail = Buffer.from(email).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

  try {
    const res = await gmail.users.messages.send({
      userId: 'me',
      requestBody: {
        raw: encodedEmail,
      },
    });
    console.log('Email sent successfully:', res.data);
  } catch (err) {
    console.error('Error sending email:', err);
    throw err;
  }
}

async function main() {
  try {
    const tokens = await getAccessToken();
    oauth2Client.setCredentials(tokens);
    await sendTestEmail(oauth2Client);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
}

main();