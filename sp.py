from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1. Launch the browser
    browser = p.chromium.launch(headless=False)
    
    # 2. Create context with geolocation and permissions configured
    context = browser.new_context(
        geolocation={"latitude": 48.8584, "longitude": 2.2945}, # Paris (Eiffel Tower)
        permissions=["geolocation"]
    )
    
    page = context.new_page()
    
    # 3. Test the location
    page.goto("https://gps-coordinates.net")
    page.wait_for_timeout(5000) # Pause to view the changes visually
    
    # 4. Dynamically change location during the test execution
    context.set_geolocation({"latitude": 40.7829, "longitude": -73.9654}) # New York (Central Park)
    page.reload()
    page.wait_for_timeout(5000)

    browser.close()
