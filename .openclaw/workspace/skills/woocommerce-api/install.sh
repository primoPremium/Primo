#!/bin/bash

# Create necessary directories
mkdir -p logs
mkdir -p assets/request-templates
mkdir -p assets/postman

# Install dependencies
npm install

# Check for environment variables
if [ ! -f ../.env ]; then
  echo "Creating sample .env file..."
  cat > ../.env << EOL
# WooCommerce API Configuration
WP_WOO_API_KEY=your_key_here
WP_WOO_API_SECRET=your_secret_here
EOL
fi

echo "Installation complete! Please ensure your .env contains WP_WOO_API_KEY and WP_WOO_API_SECRET"