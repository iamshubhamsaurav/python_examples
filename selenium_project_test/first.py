import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

title = driver.title

time.sleep(2)

userName = driver.find_element(by=By.NAME,value="username")

password = driver.find_element(by=By.NAME,value="password")

submitButton = driver.find_element(by=By.CSS_SELECTOR,value="button")

time.sleep(2)

userName.send_keys("Admin")

time.sleep(2)

password.send_keys("admin123")

time.sleep(2)

submitButton.click()

time.sleep(2)

driver.quit()
