#!/usr/bin/env python3
"""
Generate placeholder images for CosmosCost Dark Chrome theme.
Requires PIL/Pillow: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont

# Color scheme from VS Code theme
COLORS = {
    'background': '#0f172a',
    'purple': '#a78bfa',
    'orange': '#f59e6d',
    'blue': '#60a5fa',
    'pink': '#ec4899',
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_image(width, height, color1, color2, filename):
    """Create a horizontal gradient image."""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)

    for x in range(width):
        ratio = x / width
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line([(x, 0), (x, height)], fill=(r, g, b))

    image.save(filename)
    print(f"Created: {filename}")

def create_solid_image(width, height, color, filename):
    """Create a solid color image."""
    image = Image.new('RGB', (width, height), hex_to_rgb(color))
    image.save(filename)
    print(f"Created: {filename}")

def create_icon(size, filename):
    """Create a simple icon with the theme colors."""
    image = Image.new('RGB', (size, size), hex_to_rgb(COLORS['background']))
    draw = ImageDraw.Draw(image)

    # Draw a stylized "C" for CosmosCost
    margin = size // 8

    # Purple circle background
    draw.ellipse([margin, margin, size - margin, size - margin],
                 fill=hex_to_rgb(COLORS['purple']))

    # Orange accent
    inner_margin = margin + size // 6
    draw.ellipse([inner_margin, inner_margin, size - inner_margin, size - inner_margin],
                 fill=hex_to_rgb(COLORS['orange']))

    # Cut out to make "C" shape
    cutout = size // 3
    draw.rectangle([size - cutout, size // 3, size, 2 * size // 3],
                   fill=hex_to_rgb(COLORS['background']))

    image.save(filename)
    print(f"Created: {filename}")

def main():
    """Generate all required images for the Chrome theme."""
    images_dir = 'images'

    # Frame and toolbar images (gradient from dark blue to slightly lighter)
    create_gradient_image(1000, 100, COLORS['background'], '#1e293b',
                         f'{images_dir}/theme_frame.png')
    create_solid_image(1000, 200, COLORS['background'],
                      f'{images_dir}/theme_toolbar.png')
    create_solid_image(1000, 100, COLORS['background'],
                      f'{images_dir}/theme_tab_background.png')

    # New Tab Page background (subtle gradient with accent)
    create_gradient_image(1920, 1080, COLORS['background'], '#1e293b',
                         f'{images_dir}/theme_ntp_background.png')

    # Icons
    create_icon(16, f'{images_dir}/icon16.png')
    create_icon(48, f'{images_dir}/icon48.png')
    create_icon(128, f'{images_dir}/icon128.png')

    print("\nAll images generated successfully!")
    print("You can now load the theme in Chrome by going to:")
    print("chrome://extensions/ -> Enable Developer Mode -> Load unpacked")

if __name__ == '__main__':
    main()
