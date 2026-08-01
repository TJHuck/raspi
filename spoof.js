const { chromium } = require('playwright');

(async () => {
  // 1. Launch a visible browser instance
  const browser = await chromium.launch({ 
    headless: true,
    args: ['--start-maximized'] 
  });

  // 2. Create an isolated profile with injected location data
  const context = await browser.newContext({
    // Example: Coordinates for Tokyo, Japan
    geolocation: { latitude: 35.6762, longitude: 139.6503 }, 
    
    // Explicitly grant permission so Google doesn't show a popup block
    permissions: ['geolocation'],
    
    // Optional: Match the timezone and language to make the spoof realistic
    timezoneId: 'America/Detroit',
    locale: 'en-US'
  });

  // 3. Open a new window and navigate to Google
  const page = await context.newPage();
  
  // Go to Google Maps to visually verify the spoof works
  await page.goto('https://google.com');

})();
