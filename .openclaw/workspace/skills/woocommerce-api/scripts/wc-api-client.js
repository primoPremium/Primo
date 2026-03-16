const OAuth = require('oauth-1.0a');
const crypto = require('crypto');
const fetch = require('node-fetch');
const fs = require('fs');
const path = require('path');

class WooCommerceAPI {
    constructor(config) {
        this.baseURL = config.storeURL;
        this.consumerKey = config.consumerKey;
        this.consumerSecret = config.consumerSecret;
        this.logFile = path.join(__dirname, '../logs/api.log');

        this.oauth = new OAuth({
            consumer: {
                key: this.consumerKey,
                secret: this.consumerSecret
            },
            signature_method: 'HMAC-SHA256',
            hash_function(baseString, key) {
                return crypto
                    .createHmac('sha256', key)
                    .update(baseString)
                    .digest('base64');
            }
        });
    }

    async logRequest(method, endpoint, status, statusText) {
        const timestamp = new Date().toISOString();
        const logEntry = `[${timestamp}] ${method} ${endpoint} - ${status} ${statusText}\n`;
        
        fs.appendFileSync(this.logFile, logEntry);
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}/wp-json/wc/v3${endpoint}`;
        
        const requestData = {
            url: url,
            method: options.method || 'GET'
        };

        const oauthHeader = this.oauth.toHeader(this.oauth.authorize(requestData));

        try {
            const response = await fetch(url, {
                ...options,
                headers: {
                    ...oauthHeader,
                    'Content-Type': 'application/json',
                    ...options.headers
                }
            });

            await this.logRequest(options.method || 'GET', endpoint, response.status, response.statusText);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            await this.logRequest(options.method || 'GET', endpoint, 'ERROR', error.message);
            throw error;
        }
    }

    // Product Methods
    async getProducts(params = {}) {
        return this.request('/products?' + new URLSearchParams(params));
    }

    async getProduct(id) {
        return this.request(`/products/${id}`);
    }

    async createProduct(data) {
        return this.request('/products', {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    // Order Methods
    async getOrders(params = {}) {
        return this.request('/orders?' + new URLSearchParams(params));
    }

    async getOrder(id) {
        return this.request(`/orders/${id}`);
    }

    async updateOrder(id, data) {
        return this.request(`/orders/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    // Customer Methods
    async getCustomers(params = {}) {
        return this.request('/customers?' + new URLSearchParams(params));
    }

    async getCustomer(id) {
        return this.request(`/customers/${id}`);
    }

    // Report Methods
    async getSalesReport(params = {}) {
        return this.request('/reports/sales?' + new URLSearchParams(params));
    }

    async getTopSellers(params = {}) {
        return this.request('/reports/top_sellers?' + new URLSearchParams(params));
    }
}

module.exports = WooCommerceAPI;