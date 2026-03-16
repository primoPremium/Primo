const https = require('https');

function getProducts(config) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'premiummedscollective.com',
            path: `/wp-json/wc/v3/products?consumer_key=${config.apiKey}&consumer_secret=${config.apiSecret}&orderby=popularity&order=desc&per_page=12`,
            method: 'GET'
        };

        const req = https.request(options, (res) => {
            let data = '';

            res.on('data', (chunk) => {
                data += chunk;
            });

            res.on('end', () => {
                resolve(JSON.parse(data));
            });
        });

        req.on('error', (error) => {
            reject(error);
        });

        req.end();
    });
}

// Export the function
module.exports = { getProducts };