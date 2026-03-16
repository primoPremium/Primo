class WordPressAPI {
    constructor(config) {
        this.baseURL = config.apiURL;
        this.auth = Buffer.from(`${config.username}:${config.password}`).toString('base64');
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const headers = {
            'Authorization': `Basic ${this.auth}`,
            'Content-Type': 'application/json',
            ...options.headers
        };

        try {
            const response = await fetch(url, {
                ...options,
                headers
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`API Error (${endpoint}):`, error.message);
            throw error;
        }
    }

    // Post Methods
    async getPosts(params = {}) {
        return this.request('/posts?' + new URLSearchParams(params));
    }

    async createPost(data) {
        return this.request('/posts', {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async updatePost(id, data) {
        return this.request(`/posts/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    // Page Methods
    async getPages(params = {}) {
        return this.request('/pages?' + new URLSearchParams(params));
    }

    async createPage(data) {
        return this.request('/pages', {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    // Media Methods
    async getMedia(params = {}) {
        return this.request('/media?' + new URLSearchParams(params));
    }

    async uploadMedia(file, data = {}) {
        const formData = new FormData();
        formData.append('file', file);
        
        Object.entries(data).forEach(([key, value]) => {
            formData.append(key, value);
        });

        return this.request('/media', {
            method: 'POST',
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            body: formData
        });
    }

    // User Methods
    async getUsers(params = {}) {
        return this.request('/users?' + new URLSearchParams(params));
    }

    async getCurrentUser() {
        return this.request('/users/me');
    }
}

module.exports = WordPressAPI;