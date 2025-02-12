from time import sleep

from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:3000/adminlogin")

sleep(3)

name  = driver.find_element(By.XPATH,"//*[@id='email']")
name.send_keys("admin")

sleep(3)

mail = driver.find_element(By.XPATH,"//*[@id='password']")
mail.send_keys("Admin123")

sleep(2)


chebox = driver.find_element(By.XPATH,"//*[@id='root']/main/div/form/label/span[1]/input")
chebox.click()

sleep(2)

button = driver.find_element(By.XPATH,"//*[@id='submit']")
button.click()

sleep(5)
#
# button2 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[9]/div[3]/button[1]")
# button2.click()
#
# sleep(15)
#
# searchbar = driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/button[1]")
# searchbar.click()


driver.quit()