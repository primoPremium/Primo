const WooCommerceAPI = require('./wc-api-client.js');

class WooCommerceAnalytics {
    constructor(client) {
        this.client = client;
    }

    async getTopSellingProducts(limit = 12, category = null) {
        const products = await this.client.getProducts({
            orderby: 'total_sales',
            order: 'desc',
            per_page: limit,
            category: category
        });

        return products.map(product => ({
            id: product.id,
            name: product.name,
            total_sales: product.total_sales,
            price: product.price,
            regular_price: product.regular_price,
            sale_price: product.sale_price,
            category: product.categories[0]?.name || 'Uncategorized'
        }));
    }

    async getSalesTrendsByCategory(days = 30) {
        const orders = await this.client.getOrders({
            after: new Date(Date.now() - days * 24 * 60 * 60 * 1000).toISOString()
        });

        const categorySales = {};
        orders.forEach(order => {
            order.line_items.forEach(item => {
                const category = item.categories?.[0]?.name || 'Uncategorized';
                if (!categorySales[category]) {
                    categorySales[category] = {
                        total_sales: 0,
                        quantity: 0,
                        revenue: 0
                    };
                }
                categorySales[category].total_sales++;
                categorySales[category].quantity += item.quantity;
                categorySales[category].revenue += parseFloat(item.total);
            });
        });

        return categorySales;
    }

    async getInventoryAlerts(lowStockThreshold = 5) {
        const products = await this.client.getProducts({
            stock_status: 'instock',
            per_page: 100
        });

        return products.filter(product => 
            product.manage_stock && 
            product.stock_quantity <= lowStockThreshold
        ).map(product => ({
            id: product.id,
            name: product.name,
            stock: product.stock_quantity,
            category: product.categories[0]?.name || 'Uncategorized'
        }));
    }
}

module.exports = WooCommerceAnalytics;