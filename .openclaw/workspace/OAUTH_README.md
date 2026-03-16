# Simplified Google OAuth Flow Guide

This guide explains how to set up and use the simplified OAuth flow for Google APIs.

## Prerequisites

1. Install required packages:
```bash
pip install google-auth-oauthlib google-auth
```

2. Set up Google Cloud Project and OAuth 2.0 Client ID:
   - Go to Google Cloud Console (https://console.cloud.google.com)
   - Create a new project or select existing project
   - Enable the APIs you need (e.g., Gmail API, Calendar API)
   - Go to "Credentials" page
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop application"
   - Download the client configuration file and save as `credentials.json`

## Files

- `oauth_flow.py`: Main OAuth flow script
- `credentials.json`: Your OAuth client secrets (downloaded from Google Cloud Console)
- `token.json`: Stored credentials (automatically created after first authentication)

## Usage

1. Place your `credentials.json` in the same directory as `oauth_flow.py`
2. Run the script:
```bash
python oauth_flow.py
```
3. First time: Browser will open for authentication
4. After authentication: Credentials stored in `token.json`

## Security Notes

- Keep `credentials.json` and `token.json` secure
- Never commit these files to version control
- Store them in a secure location with restricted permissions
- Set appropriate file permissions:
```bash
chmod 600 credentials.json token.json
```

## Non-interactive Usage

After initial authentication, the script will use stored credentials and refresh them automatically when needed. No browser interaction required for subsequent runs.

## Customization

Edit the `SCOPES` list in `oauth_flow.py` to add or remove API scopes as needed.

## Troubleshooting

1. If authentication fails:
   - Verify `credentials.json` is valid and contains correct client configuration
   - Ensure required API services are enabled in Google Cloud Console
   - Check if scopes match enabled APIs

2. If token refresh fails:
   - Delete `token.json` and re-authenticate
   - Verify your application still has API access
   - Check if consent screen configuration is valid