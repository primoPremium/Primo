const WordPressAPI = require('./api-client.js');

const api = new WordPressAPI({
    apiURL: process.env.STORE_URL + '/wp-json/wp/v2',
    username: process.env.STORE_USER,
    password: process.env.STORE_PASS
});

async function listRecentPosts() {
    try {
        console.log('Fetching 3 most recent posts...');
        const posts = await api.request('/posts?per_page=3&orderby=date&order=desc');
        console.log('\nRecent Posts:');
        posts.forEach((post, i) => {
            console.log(`\n${i + 1}. ${post.title.rendered}`);
            console.log(`Published: ${post.date}`);
            console.log(`Status: ${post.status}`);
            console.log(`Link: ${post.link}`);
        });
    } catch (error) {
        console.error('Error:', error.message);
        // Add auth debugging
        console.log('\nAuth Debug:');
        console.log('API URL:', process.env.STORE_URL + '/wp-json/wp/v2');
        console.log('Username set:', !!process.env.STORE_USER);
        console.log('Password set:', !!process.env.STORE_PASS);
    }
}

listRecentPosts();