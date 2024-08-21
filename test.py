from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Path to your Chrome User Data and Profile
user_data_dir = "C:/Users/samru/AppData/Local/Google/Chrome/User Data"
profile_dir = "Profile 4"  # Change to your profile directory

# Setup Chrome driver with existing user profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_dir}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Go to the website
    driver.get("https://www.truscholar.io/")
    time.sleep(3)  # Wait for the page to load

    # Click on the specified xpath
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/div/div[3]/div/ul/li/a/span')
    login_button.click()
    time.sleep(9)  # Wait for the next page to load

    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/nav/div/div/div/ul[1]/div[1]/div[2]/span')
    button.click()
    buttonlearner = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/nav/div/div/div/ul[1]/div[2]/div/div/div/a[2]/div/span')
    buttonlearner.click()
    inputtext = input("Please enter the input for the field: ")
    input =  driver.find_element(By.XPATH, '//*[@id="mui-32450"]')
    input.send_keys(inputtext)
    
finally:
    # Close the browser after the operations
    time.sleep(5)  # Wait to observe the result
    driver.quit()









