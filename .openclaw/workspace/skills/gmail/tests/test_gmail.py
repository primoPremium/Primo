import unittest
from unittest.mock import MagicMock, patch
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.gmail_client import GmailClient

class TestGmailClient(unittest.TestCase):
    def setUp(self):
        self.client = GmailClient()
        
    @patch('src.gmail_client.build')
    def test_read_messages(self, mock_build):
        """Test reading messages."""
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        mock_messages = {
            'messages': [
                {'id': '123'},
                {'id': '456'}
            ]
        }
        
        mock_service.users().messages().list().execute.return_value = mock_messages
        mock_service.users().messages().get().execute.return_value = {
            'id': '123',
            'snippet': 'Test message'
        }
        
        messages = self.client.read_messages(limit=2)
        self.assertEqual(len(messages), 2)
        
    @patch('src.gmail_client.build')
    def test_send_email(self, mock_build):
        """Test sending email."""
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        result = self.client.send_email(
            to='test@example.com',
            subject='Test Subject',
            body='Test Body'
        )
        
        self.assertTrue(result)
        mock_service.users().messages().send.assert_called_once()
        
    @patch('src.gmail_client.build')
    def test_send_email_with_attachment(self, mock_build):
        """Test sending email with attachment."""
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        with open('test_attachment.txt', 'w') as f:
            f.write('Test content')
            
        try:
            result = self.client.send_email(
                to='test@example.com',
                subject='Test Subject',
                body='Test Body',
                attachments=['test_attachment.txt']
            )
            
            self.assertTrue(result)
            mock_service.users().messages().send.assert_called_once()
        finally:
            os.remove('test_attachment.txt')
            
if __name__ == '__main__':
    unittest.main()