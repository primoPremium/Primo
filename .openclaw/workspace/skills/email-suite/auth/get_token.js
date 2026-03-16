const { google } = require('googleapis');
const http = require('http');
const url = require('url');
const open = require('open');

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  'http://localhost:3000/oauth2callback'
);

// Generate a url for OAuth2 consent
const authUrl = oauth2Client.generateAuthUrl({
  access_type: 'offline',
  scope: ['https://www.googleapis.com/auth/gmail.send']
});

console.log('Opening auth URL...');

// Create temporary server to handle the OAuth2 callback
const server = http.createServer(async (req, res) => {
  try {
    const queryObject = url.parse(req.url, true).query;
    if (queryObject.code) {
      const { tokens } = await oauth2Client.getToken(queryObject.code);
      console.log('Access Token:', tokens.access_token);
      console.log('Refresh Token:', tokens.refresh_token);
      res.end('Authentication successful! You can close this window.');
      server.close();
    }
  } catch (e) {
    console.error('Error getting tokens:', e);
    res.end('Authentication failed! Please check the console.');
    server.close();
  }
}).listen(3000, () => {
  console.log('Temporary server listening on port 3000');
  open(authUrl);
});