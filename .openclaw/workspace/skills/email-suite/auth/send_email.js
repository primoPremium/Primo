const { google } = require('googleapis');
const fs = require('fs');

const credentials = {
  client_id: process.env.GOOGLE_CLIENT_ID,
  client_secret: process.env.GOOGLE_CLIENT_SECRET,
  redirect_uri: 'http://localhost:3000/oauth2callback'
};

const oauth2Client = new google.auth.OAuth2(
  credentials.client_id,
  credentials.client_secret,
  credentials.redirect_uri
);

// Use refresh token if available
const token = {
  access_token: process.env.GOOGLE_ACCESS_TOKEN,
  refresh_token: process.env.GOOGLE_REFRESH_TOKEN,
  scope: 'https://www.googleapis.com/auth/gmail.send',
  token_type: 'Bearer'
};

oauth2Client.setCredentials(token);

const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

const email = [
  'From: "Premium Meds" <premiummedscollective@gmail.com>',
  'To: premiummedsoc@gmail.com',
  'Subject: Let\'s meetup on Primo',
  '',
  'Hey Nick, we should probably sync up so I can get a better idea of your budget and expectations. There are so many things happening in ai right now that could empower primo from the latest update to openclaw (plugins), to Google suite cli, memory fixes, local vs headless experiences (cloud ec2 vs macmini), to model subscriptions vs local llm install, to the extreme costs in advertising campaign management and perhaps the most expensive topic of all: advertising.'
].join('\n');

const encodedEmail = Buffer.from(email).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

gmail.users.messages.send({
  userId: 'me',
  requestBody: {
    raw: encodedEmail
  }
}, (err, res) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log('Email sent:', res.data);
});