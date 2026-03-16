const Gmail = require('../scripts/gmail');
const config = require('../config/default.json');

async function readEmails() {
  try {
    const gmail = new Gmail(config.gmail);
    
    // List recent emails
    const messages = await gmail.listMessages({
      maxResults: 5,
      labelIds: ['INBOX']
    });

    console.log('Recent messages:', messages);

    // Read first email details
    if (messages.length > 0) {
      const email = await gmail.getMessage(messages[0].id);
      console.log('First email details:', email);
    }

  } catch (error) {
    console.error('Error reading emails:', error);
  }
}

readEmails();