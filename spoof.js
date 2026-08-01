const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({
    // Emulate specific coordinates (e.g., Paris, France)
    geolocation: { latitude: 48.8566, longitude: 2.3522 },
    permissions: ['geolocation']
  });
  const page = await context.newPage();
  await page.goto('https://google.com');
})();
