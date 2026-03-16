const Gmail = require('../scripts/gmail');
const config = require('../config/default.json');

async function sendEmail() {
  try {
    const gmail = new Gmail(config.gmail);
    
    const messageOptions = {
      to: 'recipient@example.com',
      subject: 'Test Email from OpenClaw Gmail Skill',
      body: 'This is a test email sent using the OpenClaw Gmail skill.\n\nBest regards,\nOpenClaw'
    };

    const result = await gmail.sendMessage(messageOptions);
    console.log('Email sent successfully:', result);

  } catch (error) {
    console.error('Error sending email:', error);
  }
}

sendEmail();