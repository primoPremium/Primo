# WooCommerce Integration Configuration

## API Credentials
Environment variables used for WooCommerce API access:
- API Key: `WP_WOO_API_KEY`
- API Secret: `WP_WOO_API_SECRET`

## Base Configuration
- Store URL: https://premiummedscollective.com
- API Version: v3
- Endpoint Base: /wp-json/wc/v3

## Authentication
Using API key authentication with existing cronjob configuration.
No additional setup required as credentials are already configured in environment.

## Usage Notes
- Use existing environment variables for all API calls
- Maintain compatibility with existing cronjob implementation
- Follow security protocols from credential_handling.md