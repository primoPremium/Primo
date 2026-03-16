#!/usr/bin/env python3

import os
import unittest
from unittest.mock import MagicMock, patch
from gmail_client import GmailClient

class TestGmailClient(unittest.TestCase):
    def setUp(self):
        self.client = GmailClient(
            client_id="test_client_id",
            client_secret="test_client_secret",
            redirect_uri="http://localhost:3000/oauth2callback",
            token_path="test_token.pickle"
        )
        
    @patch('gmail_client.build')
    @patch('gmail_client.InstalledAppFlow')
    def test_authentication(self, mock_flow, mock_build):
        # Mock OAuth2 flow
        mock_flow.from_client_config.return_value.run_local_server.return_value = MagicMock()
        mock_build.return_value = MagicMock()
        
        # Test authentication
        self.client.authenticate()
        self.assertIsNotNone(self.client.service)
        
    @patch('gmail_client.build')
    def test_list_messages(self, mock_build):
        # Mock Gmail API response
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_response = {
            'messages': [
                {'id': '123', 'threadId': 'thread123'},
                {'id': '456', 'threadId': 'thread456'}
            ]
        }
        mock_service.users().messages().list().execute.return_value = mock_response
        mock_service.users().messages().get().execute.return_value = {
            'id': '123',
            'snippet': 'Test email'
        }
        
        self.client.service = mock_service
        messages = self.client.list_messages(max_results=2)
        
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]['id'], '123')
        
    @patch('gmail_client.build')
    def test_send_message(self, mock_build):
        # Mock Gmail API response
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_service.users().messages().send().execute.return_value = {
            'id': 'sent123',
            'labelIds': ['SENT']
        }
        
        self.client.service = mock_service
        result = self.client.send_message(
            to="test@example.com",
            subject="Test Subject",
            body="Test Body"
        )
        
        self.assertEqual(result['id'], 'sent123')
        
    def tearDown(self):
        # Clean up test token file if it exists
        if os.path.exists("test_token.pickle"):
            os.remove("test_token.pickle")

if __name__ == '__main__':
    unittest.main()