#!/usr/bin/env node
const { saveTokens } = require('../src/token_manager');

async function initializeTokens() {
  // Initial token structure based on environment variables
  const tokens = {
    client_id: process.env.GOOGLE_CLIENT_ID,
    client_secret: process.env.GOOGLE_CLIENT_SECRET,
    refresh_token: process.env.GOOGLE_REFRESH_TOKEN,
    token_uri: 'https://oauth2.googleapis.com/token',
    scopes: [
      'https://www.googleapis.com/auth/gmail.send',
      'https://www.googleapis.com/auth/gmail.modify'
    ]
  };

  try {
    await saveTokens(tokens);
    console.log('Gmail tokens initialized successfully');
  } catch (error) {
    console.error('Failed to initialize tokens:', error);
  }
}

initializeTokens();