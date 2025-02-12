from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sleep_time = 3

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")

driver.maximize_window()
sleep(sleep_time)

#by ID
get_start_button = driver.find_element(By.ID,"get_started")
get_start_button.click()
sleep(sleep_time)

driver.get("http://localhost:3000/")
driver.maximize_window()
sleep(sleep_time)

#by name
join_us_button = driver.find_element(By.NAME,"join_us")
join_us_button.click()
sleep(sleep_time)

driver.get("http://localhost:3000/")
driver.maximize_window()
sleep(sleep_time)

#by link text
link  = driver.find_element(By.LINK_TEXT,"LOGIN")
link.click()

sleep(sleep_time)

#by link text
link  = driver.find_element(By.PARTIAL_LINK_TEXT,"Don't")
link.click()
sleep(sleep_time)

driver.quit()
