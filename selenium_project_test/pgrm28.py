from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
search_box = driver.find_element(By.NAME, 'q')
sleep(2)
search_box.send_keys("Selenium")
sleep(2)
search_box.submit()
sleep(2)
#driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
sleep(2)
driver.close()