# WooCommerce API Setup Process

## Generating API Credentials
1. Access WordPress admin at premiummedscollective.com/wp-admin
2. Navigate to: WooCommerce → Settings → Advanced → REST API
3. Click "Add Key"
4. Configure new key:
   - Description: "Sales Report Agent"
   - User: Select appropriate user
   - Permissions: Read (for report generation)
   - Note: Never use "write" permissions unless absolutely necessary

## Required Credentials
- Consumer Key
- Consumer Secret
- These are different from WordPress admin or CLI credentials

## Security Notes
- Store credentials securely in .env
- Never commit API keys to repositories
- Use read-only permissions when possible
- Regularly rotate keys

## Implementation
Once generated, add to .env:
```
WOOCOMMERCE_CONSUMER_KEY="your_consumer_key"
WOOCOMMERCE_CONSUMER_SECRET="your_consumer_secret"
```

## Verification Process
1. Test API access with read-only call
2. Verify data retrieval
3. Document successful connection