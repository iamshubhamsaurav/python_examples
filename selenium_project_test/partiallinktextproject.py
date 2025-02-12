from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sleep_time = 3

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")

sleep(sleep_time)


link2 = driver.find_element(By.PARTIAL_LINK_TEXT,"Shadow")
link2.click()

sleep(sleep_time)


driver.quit()
