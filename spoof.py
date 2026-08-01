from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def get_coordinate(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get coordinates from the user via terminal
print("--- Selenium Geolocation Faker ---")
latitude = get_coordinate("Enter Latitude (e.g., 40.7128): ")
longitude = get_coordinate("Enter Longitude (e.g., -74.0060): ")
accuracy = 100

print(f"\nLaunching Chrome with location set to: {latitude}, {longitude}...")

# Initialize Chrome driver
driver = webdriver.Chrome()

# Execute CDP command to override geolocation
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
    "latitude": latitude,
    "longitude": longitude,
    "accuracy": accuracy
})

# Grant geolocation permissions to the site automatically
driver.execute_cdp_cmd("Browser.grantPermissions", {
    "permissions": ["geolocation"]
})

# Navigate to verify
driver.get("https://google.com")
time.sleep(10)  # Kept open longer so you can inspect the map

driver.quit()
