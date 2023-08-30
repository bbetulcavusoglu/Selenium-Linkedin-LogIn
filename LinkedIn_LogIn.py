import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = r"C:\Users\...\Drivers" #Enter the path where your driver is located

# Start the Selenium webdriver
driver = webdriver.Chrome()

url = "https://www.linkedin.com/home"
# Go to LinkedIn
driver.get(url)

# Web sayfasını tam ekran yapın
driver.maximize_window()

#Your email and password
email="#Enter the your email adres"
password= "#Enter the your password"

# Enter your email
email_input = driver.find_element(By.ID,"session_key")
email_input.send_keys(email)
wait = WebDriverWait(driver, 10)

# Enter your password
password_input = driver.find_element(By.ID,"session_password")
password_input.send_keys(password)
wait = WebDriverWait(driver, 10)

# Click the login button
login_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
login_button.click()
wait = WebDriverWait(driver, 10)
time.sleep(5)

# Web sürücüsünü kapatın
driver.close()
