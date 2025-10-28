const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const sizes = [16, 32, 48, 64, 128, 256, 512];
const inputDir = path.join(__dirname, 'images');

async function convertSVGtoPNG() {
  for (const size of sizes) {
    const svgFile = path.join(inputDir, `cosmoscost-${size}.svg`);
    const pngFile = path.join(inputDir, `cosmoscost-${size}.png`);

    if (fs.existsSync(svgFile)) {
      try {
        await sharp(svgFile)
          .resize(size, size)
          .png()
          .toFile(pngFile);
        console.log(`✓ Converted cosmoscost-${size}.svg to PNG`);
      } catch (error) {
        console.error(`✗ Error converting cosmoscost-${size}.svg:`, error.message);
      }
    }
  }

  // Also create icon16 if we have a 16px version
  const icon16Source = path.join(inputDir, 'cosmoscost-16.svg');
  const icon16Target = path.join(inputDir, 'icon16.png');

  // Use 32px as source for 16px if 16px doesn't exist
  const sourceFile = fs.existsSync(icon16Source) ? icon16Source : path.join(inputDir, 'cosmoscost-32.svg');

  if (fs.existsSync(sourceFile)) {
    try {
      await sharp(sourceFile)
        .resize(16, 16)
        .png()
        .toFile(icon16Target);
      console.log('✓ Created icon16.png');
    } catch (error) {
      console.error('✗ Error creating icon16.png:', error.message);
    }
  }
}

convertSVGtoPNG().then(() => {
  console.log('\nConversion complete!');
}).catch(error => {
  console.error('Error:', error);
  process.exit(1);
});
