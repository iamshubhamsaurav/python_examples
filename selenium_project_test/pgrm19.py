from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sleep_time = 3

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

sleep(sleep_time)

#by classname
box1 = driver.find_element(By.TAG_NAME,"input")
box1.send_keys("standard_user")
sleep(sleep_time)

#by id
box2 = driver.find_element(By.CLASS_NAME,"input_error.form_input[placeholder='Password']")
box2.send_keys("secret_sauce")
sleep(sleep_time)

#by tag name
submit = driver.find_element(By.CLASS_NAME,"submit-button.btn_action")
submit.click()

sleep(sleep_time+1)

driver.quit()
