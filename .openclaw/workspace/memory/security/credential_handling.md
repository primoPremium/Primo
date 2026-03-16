# Credential Handling Guidelines

## Environment Variable Standards

### WordPress/WooCommerce Credentials
```env
WOOCOMMERCE_CONSUMER_KEY=your_consumer_key
WOOCOMMERCE_CONSUMER_SECRET=your_consumer_secret
WORDPRESS_API_URL=https://premiummedscollective.com/wp-json
```

### Configuration File References
- Location: `~/.openclaw/config/credentials/`
- Format: YAML configuration files
- Permissions: 600 (user read/write only)

## Security Protocols

1. NEVER:
   - Share credentials in chat messages
   - Store passwords in code or scripts
   - Commit sensitive data to version control
   - Log sensitive information

2. ALWAYS:
   - Use environment variables for sensitive data
   - Reference credentials through secure configuration
   - Use secure parameter storage for persistent data
   - Implement role-based access control

## Implementation Guidelines

### Code Pattern
```python
import os

# Correct way
api_key = os.environ.get('WOOCOMMERCE_CONSUMER_KEY')

# Never do this
api_key = "actual_key_here"  # WRONG
```

### Configuration Pattern
```yaml
# config.yaml
api:
  key_env: WOOCOMMERCE_CONSUMER_KEY
  secret_env: WOOCOMMERCE_CONSUMER_SECRET
```

## Audit Trail Requirements

1. Track all credential access
2. Log access patterns (not credentials)
3. Monitor for unauthorized access attempts
4. Regular security audits

## Emergency Procedures

1. Credential compromise response plan
2. Key rotation procedures
3. Access revocation process
4. Incident reporting guidelines

## Validation Checklist

- [ ] Environment variables configured
- [ ] Secure storage implemented
- [ ] Access logging enabled
- [ ] Monitoring in place
- [ ] Backup procedures documented