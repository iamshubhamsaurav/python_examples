from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sleep_time = 3

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")

sleep(sleep_time)

#by classname
link1 = driver.find_element(By.CLASS_NAME,"MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeMedium.css-73u334-MuiButtonBase-root-MuiIconButton-root")
link1.click()
sleep(sleep_time)

#by tag name
signin = driver.find_element(By.TAG_NAME,"button")
signin.click()

sleep(sleep_time+1)


driver.quit()
