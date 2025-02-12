from time import sleep

from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

sleep(3)

button1 = driver.find_element(By.XPATH,"//input[@id='small-searchterms' or @placeholder='Search']")

button1.click()

button1.send_keys('Computer')

sleep(5)

btn2 = driver.find_element(By.XPATH,"//*[contains(@id,'cart')]")
btn2.click()

sleep(7)
#
# button2 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[9]/div[3]/button[1]")
# button2.click()
#
# sleep(15)
#
# searchbar = driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/button[1]")
# searchbar.click()


driver.quit()