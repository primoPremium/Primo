const https = require('https');

const url = 'https://premiummedscollective.com/wp-json/wp/v2/posts?per_page=3&orderby=date&order=desc';

https.get(url, (resp) => {
  let data = '';

  resp.on('data', (chunk) => {
    data += chunk;
  });

  resp.on('end', () => {
    const posts = JSON.parse(data);
    console.log('\nRecent Posts:');
    posts.forEach((post, i) => {
      console.log(`\n${i + 1}. ${post.title.rendered}`);
      console.log(`Published: ${post.date}`);
      console.log(`Link: ${post.link}`);
    });
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});