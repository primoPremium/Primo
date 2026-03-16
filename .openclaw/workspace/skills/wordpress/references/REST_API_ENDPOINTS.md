# WordPress REST API Endpoints Reference

## Core Endpoints

### Posts
- `GET /wp/v2/posts` - List posts
- `POST /wp/v2/posts` - Create post
- `GET /wp/v2/posts/{id}` - Get post
- `PUT /wp/v2/posts/{id}` - Update post
- `DELETE /wp/v2/posts/{id}` - Delete post

### Pages
- `GET /wp/v2/pages` - List pages
- `POST /wp/v2/pages` - Create page
- `GET /wp/v2/pages/{id}` - Get page
- `PUT /wp/v2/pages/{id}` - Update page
- `DELETE /wp/v2/pages/{id}` - Delete page

### Media
- `GET /wp/v2/media` - List media
- `POST /wp/v2/media` - Upload media
- `GET /wp/v2/media/{id}` - Get media item
- `PUT /wp/v2/media/{id}` - Update media
- `DELETE /wp/v2/media/{id}` - Delete media

### Users
- `GET /wp/v2/users` - List users
- `POST /wp/v2/users` - Create user
- `GET /wp/v2/users/{id}` - Get user
- `PUT /wp/v2/users/{id}` - Update user
- `DELETE /wp/v2/users/{id}` - Delete user

### Categories
- `GET /wp/v2/categories` - List categories
- `POST /wp/v2/categories` - Create category
- `GET /wp/v2/categories/{id}` - Get category
- `PUT /wp/v2/categories/{id}` - Update category
- `DELETE /wp/v2/categories/{id}` - Delete category

### Tags
- `GET /wp/v2/tags` - List tags
- `POST /wp/v2/tags` - Create tag
- `GET /wp/v2/tags/{id}` - Get tag
- `PUT /wp/v2/tags/{id}` - Update tag
- `DELETE /wp/v2/tags/{id}` - Delete tag

## Authentication

### Application Passwords
1. Generate in WordPress admin: Users → Profile → Application Passwords
2. Use Basic Auth with username and application password
3. Include in API requests:
   ```
   Authorization: Basic base64(username:application_password)
   ```

### Common Parameters
- `context`: View context (view, embed, edit)
- `page`: Page number for pagination
- `per_page`: Items per page
- `search`: Search term
- `order`: Sort order (asc/desc)
- `orderby`: Sort field

## Status Codes
- 200: Success
- 201: Created
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Server error