#!/bin/bash

echo "=== System Integrity Check $(date -u) ==="
echo "----------------------------------------"

# 1. WooCommerce API Check
echo "1. API Credential Verification"
curl -s -o /dev/null -w "API Response Time: %{time_total}s\n" https://premiummedscollective.com/wp-json/wc/v3/system_status \
  -H "Authorization: Basic ${WC_AUTH_KEY}"
curl -s https://premiummedscollective.com/wp-json/wc/v3/system_status \
  -H "Authorization: Basic ${WC_AUTH_KEY}" | jq .

# 2. Connection Testing
echo -e "\n2. Connection Testing"
curl -s -o /dev/null -w "SSL Certificate Status: %{ssl_verify_result}\nHTTPS Response Time: %{time_total}s\n" \
  https://premiummedscollective.com/

# 3. Rate Limit Check
echo -e "\n3. Rate Limit Status"
curl -I -s https://premiummedscollective.com/wp-json/wc/v3/products \
  -H "Authorization: Basic ${WC_AUTH_KEY}" | grep "X-RateLimit"

# 4. Data Integrity
echo -e "\n4. Data Integrity Check"
curl -s https://premiummedscollective.com/wp-json/wc/v3/reports/products/totals \
  -H "Authorization: Basic ${WC_AUTH_KEY}"