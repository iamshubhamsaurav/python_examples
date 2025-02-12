#Difference between text and get attribute
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
sleep(2)

email_box = driver.find_element(By.XPATH, "//input[@id='Email']")
email_box.clear()
sleep(2)
email_box.send_keys("abc@gmail.com")
sleep(2)

print("Result of text: '", email_box.text, "'")
print("get attribute()_1: ", email_box.get_attribute('value'))
print("get attribute()_2: ", email_box.get_attribute('id'))
print("get attribute()_3: ", email_box.get_attribute('name'))
print("get attribute()_4: ", email_box.get_attribute('class'))
sleep(2)

login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("Result of text: ", login_button.text)
print("get attribute()_1: ", login_button.get_attribute('value'))
print("get attribute()_2: ", login_button.get_attribute('id'))
print("get attribute()_3: ", login_button.get_attribute('name'))
print("get attribute()_4: ", login_button.get_attribute('class'))
print("get attribute()_5: ", login_button.get_attribute('type'))

sleep(2)
driver.quit()