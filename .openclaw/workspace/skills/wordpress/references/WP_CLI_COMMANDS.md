# WP-CLI Commands Reference

## Core Management

### WordPress Core
```bash
# Update WordPress
wp core update

# Install WordPress
wp core install --url=example.com --title="Site Title" --admin_user=admin --admin_password=password --admin_email=admin@example.com

# Verify WordPress installation
wp core verify-checksums
```

### Database
```bash
# Export database
wp db export backup.sql

# Import database
wp db import backup.sql

# Optimize database
wp db optimize

# Repair database
wp db repair
```

### Plugins
```bash
# Install plugin
wp plugin install woocommerce

# Activate plugin
wp plugin activate woocommerce

# Update all plugins
wp plugin update --all

# List installed plugins
wp plugin list
```

### Themes
```bash
# Install theme
wp theme install twentytwentyfour

# Activate theme
wp theme activate twentytwentyfour

# Update all themes
wp theme update --all

# List installed themes
wp theme list
```

## Content Management

### Posts
```bash
# Create post
wp post create --post_type=post --post_title="Title" --post_content="Content" --post_status=publish

# List posts
wp post list

# Delete post
wp post delete 123
```

### Users
```bash
# Create user
wp user create bob bob@example.com --role=author

# List users
wp user list

# Delete user
wp user delete 123
```

## Maintenance

### Cache
```bash
# Flush cache
wp cache flush

# Flush rewrite rules
wp rewrite flush
```

### Updates
```bash
# Update everything
wp core update
wp plugin update --all
wp theme update --all
```

### Site Options
```bash
# Get option
wp option get home

# Update option
wp option update blogname "New Site Name"
```

## Security

### File Permissions
```bash
# Fix file permissions
wp core verify-checksums
wp maintenance-mode activate
chmod 644 wp-config.php
find . -type f -exec chmod 644 {} \\;
find . -type d -exec chmod 755 {} \\;
wp maintenance-mode deactivate
```

### SSL
```bash
# Update site URL to HTTPS
wp search-replace 'http://example.com' 'https://example.com'
```

## Remote Execution
```bash
# Via SSH
wp @staging plugin list
wp @production core update
```