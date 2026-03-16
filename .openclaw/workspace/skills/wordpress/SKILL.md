# WordPress Skill

## Overview
This skill provides core WordPress management capabilities through REST API and WP-CLI integration.

## Requirements

### Environment Variables
- `WP_CRED_URL` - WordPress site URL
- `WP_CRED_USERNAME` - WordPress API username
- `WP_CRED_PASSWORD` - WordPress API password/application password
- `WP_CLI_PATH` - Path to WordPress installation (for WP-CLI)
- `WP_CLI_USER` - WordPress CLI user
- `WP_CLI_SSH` - SSH connection string for remote WP-CLI (optional)

## Capabilities

### Core WordPress Management
- Post management (create/update/delete)
- Page management
- Media library operations
- User management
- Plugin/theme management
- Site settings configuration

### Content Management
- Draft creation and management
- Post preview capabilities
- Scheduled publishing
- Custom post types handling
- Taxonomy management

### REST API Integration
- Authentication handling
- CRUD operations for all content types
- Media upload/management
- Settings management
- User operations

### WP-CLI Support
- Remote command execution
- Bulk operations
- Database management
- Cache control
- Plugin/theme management
- User management
- Content import/export

## Security Practices
1. All credentials stored as environment variables
2. Application passwords preferred over main admin credentials
3. Minimum necessary permissions principle
4. Secure connection requirements (HTTPS)
5. Input validation and sanitization

## Usage Examples

### REST API Operations
```python
# Post Creation
wp.create_post({
    'title': 'New Post',
    'content': 'Content here',
    'status': 'draft'
})

# Media Upload
wp.upload_media('path/to/image.jpg', {
    'title': 'Featured Image'
})
```

### WP-CLI Commands
```python
# Plugin Management
wp.cli('plugin install woocommerce')
wp.cli('plugin activate woocommerce')

# Database Backup
wp.cli('db export backup.sql')
```

## Directory Structure
- `scripts/` - Python scripts for WordPress operations
- `references/` - API documentation and guides
- `assets/` - Helper files and templates

## Error Handling
- REST API errors handled with appropriate status codes
- WP-CLI command validation
- Retry mechanisms for transient failures
- Detailed error logging

## Dependencies
- requests (REST API client)
- python-dotenv (environment management)
- paramiko (SSH for remote WP-CLI)

## References
- [WordPress REST API Handbook](https://developer.wordpress.org/rest-api/)
- [WP-CLI Commands Reference](https://developer.wordpress.org/cli/commands/)