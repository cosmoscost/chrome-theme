# CosmosCost Dark - Chrome Theme

A beautiful dark theme for Google Chrome inspired by the CosmosCost Dark VS Code theme, featuring purple, orange, and blue accents.

## Color Palette

- **Primary Background**: `#0f172a` (Deep slate blue)
- **Secondary Background**: `#1e293b` (Lighter slate)
- **Purple Accent**: `#a78bfa` (Soft lavender)
- **Orange Accent**: `#f59e6d` (Warm coral)
- **Blue Accent**: `#60a5fa` (Sky blue)
- **Pink Accent**: `#ec4899` (Vibrant pink)
- **Text**: `#e2e8f0` (Light gray)

## Installation

### Method 1: Local Installation (Development)

1. Clone or download this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" (toggle in the top-right corner)
4. Click "Load unpacked"
5. Select the `cosmoscost-dark-chrome-theme` folder
6. The theme will be applied immediately

### Method 2: Chrome Web Store (Coming Soon)

Once published, you'll be able to install directly from the Chrome Web Store.

## Customization

### Regenerating Images

If you want to customize the theme images:

1. Install Python and Pillow:
   ```bash
   pip install Pillow
   ```

2. Run the image generation script:
   ```bash
   python3 create_images.py
   ```

3. Reload the extension in Chrome

### Modifying Colors

Edit `manifest.json` and update the `theme.colors` section with your preferred hex colors. Key properties:

- `frame`: Browser window background
- `toolbar`: Toolbar background
- `tab_text`: Active tab text color
- `tab_background_text`: Text in inactive tabs
- `bookmark_text`: Bookmark bar text
- `ntp_background`: New Tab Page background
- `ntp_link`: New Tab Page link color

## Distribution

### Packaging for Chrome Web Store

1. Run the package script:
   ```bash
   ./package.sh
   ```

2. This creates `cosmoscost-dark-theme.zip`

### Publishing to Chrome Web Store

1. Go to [Chrome Web Store Developer Console](https://chrome.google.com/webstore/devconsole)
2. Pay the one-time developer registration fee ($5 USD)
3. Click "New Item" and upload `cosmoscost-dark-theme.zip`
4. Fill in the store listing:
   - **Title**: CosmosCost Dark
   - **Summary**: A beautiful dark theme with purple, orange, and blue accents
   - **Description**: Use the detailed description below
   - **Category**: Themes
   - **Language**: English
   - **Icon**: Use `images/icon128.png`
   - **Screenshots**: Take screenshots of Chrome with the theme applied

5. Set pricing and distribution (free/paid, regions)
6. Submit for review

### Store Listing Description Template

```
CosmosCost Dark - A Modern Dark Theme for Chrome

Transform your Chrome browser with CosmosCost Dark, a carefully crafted theme that combines deep slate backgrounds with vibrant purple, orange, and blue accents.

✨ Features:
• Deep dark background (#0f172a) that's easy on the eyes
• Carefully selected accent colors for optimal contrast
• Consistent with the popular CosmosCost Dark VS Code theme
• Professional and modern design
• Perfect for developers and dark mode enthusiasts

🎨 Color Scheme:
• Primary: Deep slate blue
• Accents: Lavender purple, warm coral orange, sky blue
• Text: Light gray for excellent readability

Perfect for late-night coding sessions or anyone who prefers a darker browsing experience.

Based on the CosmosCost Dark VS Code theme.
```

### Screenshots Needed

Take screenshots showing:
1. Browser with tabs and toolbar
2. New Tab Page
3. Bookmarks bar
4. Incognito mode (optional)

Recommended size: 1280x800 or 1920x1080

### Review Process

- Chrome Web Store reviews typically take 1-3 business days
- You'll receive an email when your theme is approved
- After approval, it's immediately available in the store

## File Structure

```
cosmoscost-dark-chrome-theme/
├── manifest.json              # Theme configuration
├── images/
│   ├── theme_frame.png       # Browser frame background
│   ├── theme_toolbar.png     # Toolbar background
│   ├── theme_tab_background.png  # Tab background
│   ├── theme_ntp_background.png  # New Tab Page background
│   ├── icon16.png            # Extension icon (16x16)
│   ├── icon48.png            # Extension icon (48x48)
│   └── icon128.png           # Extension icon (128x128)
├── create_images.py          # Script to generate theme images
├── package.sh                # Script to create distribution package
├── .gitignore               # Git ignore file
└── README.md                # This file
```

## Technical Details

- **Manifest Version**: 3 (latest Chrome extension standard)
- **Theme Type**: Static color and image theme
- **Compatibility**: Chrome, Edge, Brave, and other Chromium-based browsers

## License

This theme is based on the CosmosCost Dark VS Code theme color palette.

## Related Projects

- [CosmosCost Dark VS Code Theme](link-to-vscode-theme) - The original inspiration

## Support

For issues or questions:
- Open an issue on GitHub
- Contact: [your-contact-info]

## Changelog

### Version 1.0.0 (Initial Release)
- Initial theme release
- Dark slate background with purple, orange, and blue accents
- Custom icons and graphics
- Full browser UI theming
