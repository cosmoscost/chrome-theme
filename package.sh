#!/bin/bash
# Package script for Chrome Web Store distribution

echo "Creating Chrome theme package..."

# Create a zip file for Chrome Web Store
zip -r cosmoscost-dark-theme.zip manifest.json images/

echo ""
echo "Package created: cosmoscost-dark-theme.zip"
echo ""
echo "To publish to Chrome Web Store:"
echo "1. Go to https://chrome.google.com/webstore/devconsole"
echo "2. Pay the one-time developer registration fee (\$5 USD)"
echo "3. Click 'New Item' and upload cosmoscost-dark-theme.zip"
echo "4. Fill in the store listing details"
echo "5. Submit for review"
echo ""
echo "The review process typically takes a few days."
