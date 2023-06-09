from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to the chromedriver executable
chromedriver_path = "path/to/chromedriver"

# Initialize the Chrome driver
driver = webdriver.Chrome(chromedriver_path)

# Open Tinder website
driver.get("https://tinder.com")

# Wait for the page to load
time.sleep(2)

# Click on the 'Log in' button
login_button = driver.find_element_by_xpath('//span[contains(text(),"Log in")]')
login_button.click()

# Wait for the login page to load
time.sleep(2)

# Enter your username or email
username_field = driver.find_element_by_name("email")
username_field.send_keys("your_username")

# Enter your password
password_field = driver.find_element_by_name("password")
password_field.send_keys("your_password")

# Press Enter to log in
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Perform further actions on the logged-in page if needed

# Close the browser
driver.quit()