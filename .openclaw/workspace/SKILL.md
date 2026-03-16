---
name: wordpress-api
description: WordPress REST API integration for accessing and managing WordPress content. Use when needing to interact with WordPress content via REST API including: (1) Posts/Pages management, (2) User data access, (3) Media management, (4) Custom post types, or (5) Any WordPress core API operations. Provides data access with proper error handling.
---

# WordPress API Skill

## Core Configuration

No need for explicit WooCommerce configuration - the WordPress application password provides necessary access.

```javascript
// Environment variables expected in .env:
STORE_USER=your-username
STORE_PASS=your-app-password
```

Get these from WordPress > Users > Your Profile > Application Passwords

## Quick Start

```javascript
const WordPressAPI = require('./scripts/api-client.js');

const api = new WordPressAPI({
    apiURL: 'https://your-site.com/wp-json/wp/v2',
    username: process.env.STORE_USER,
    password: process.env.STORE_PASS
});

// Get posts
const posts = await api.getPosts({per_page: 10});

// Get pages
const pages = await api.getPages({per_page: 10});

// Get users
const users = await api.getUsers({per_page: 10});
```

## Core Features

1. Content Management
- List/create/update posts
- List/create/update pages
- Media upload and management
- Custom post types support

2. User Management
- List users
- Get user details
- Current user info

3. Site Management
- Settings access
- Taxonomy management
- Comments moderation

## API Methods

### Posts

```javascript
// List posts
GET /wp/v2/posts

// Get single post
GET /wp/v2/posts/{id}

// Create post
POST /wp/v2/posts
{
    title: string,
    content: string,
    status: 'draft'|'publish'
}

// Update post
PUT /wp/v2/posts/{id}
{
    title?: string,
    content?: string,
    status?: string
}
```

### Pages

```javascript
// List pages
GET /wp/v2/pages

// Get single page
GET /wp/v2/pages/{id}

// Create page
POST /wp/v2/pages
{
    title: string,
    content: string,
    status: 'draft'|'publish'
}
```

### Users

```javascript
// List users
GET /wp/v2/users

// Get current user
GET /wp/v2/users/me

// Get user by ID
GET /wp/v2/users/{id}
```

## Error Handling

Common HTTP status codes:
- 200: Success
- 400: Bad request (invalid data)
- 401: Unauthorized (bad credentials)
- 403: Forbidden (insufficient permissions)
- 404: Not found
- 500: Server error

## Reference Files

- error-codes.md: Common error codes and solutions
- endpoints.md: Complete endpoint documentation
- auth-guide.md: Authentication setup guide

## Scripts

1. api-client.js
   - Core API client with authentication
   - Basic operations for posts/pages/users
   - Error handling and logging

2. media-handler.js
   - Media upload utilities
   - Image processing helpers
   - File type validation

## Assets

- request-templates/: Sample API request bodies
- postman/: API testing collection