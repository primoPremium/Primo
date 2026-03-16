const WordPressAPI = require('./api-client.js');

const api = new WordPressAPI({
    apiURL: process.env.STORE_URL + '/wp-json/wp/v2',
    username: process.env.STORE_USER,
    password: process.env.STORE_PASS
});

// Test endpoints sequentially
async function testEndpoints() {
    try {
        // Test posts endpoint
        console.log('Testing Posts API...');
        const posts = await api.request('/posts?per_page=5');
        console.log('✓ Posts API works');
        console.log(`Found ${posts.length} posts\n`);

        // Test pages endpoint
        console.log('Testing Pages API...');
        const pages = await api.request('/pages?per_page=5');
        console.log('✓ Pages API works');
        console.log(`Found ${pages.length} pages\n`);

        // Test users endpoint
        console.log('Testing Users API...');
        const users = await api.request('/users?per_page=5');
        console.log('✓ Users API works');
        console.log(`Found ${users.length} users\n`);

        // Test media endpoint
        console.log('Testing Media API...');
        const media = await api.request('/media?per_page=5');
        console.log('✓ Media API works');
        console.log(`Found ${media.length} media items\n`);

    } catch (error) {
        console.error('API Test Failed:', error.message);
    }
}

testEndpoints();