from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



sleep_time = 2

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

sleep(sleep_time)

#by name
name  = driver.find_element(By.NAME,"user-name")
name.send_keys("standard_user")

sleep(sleep_time)
#by id
mail = driver.find_element(By.ID,"password")
mail.send_keys("secret_sauce")

sleep(sleep_time)
#by ID
submitButton = driver.find_element(By.ID,"login-button")

submitButton.click()

sleep(sleep_time+2)

#by partial link text
link  = driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack")
link.click()

sleep(sleep_time)

dashboard = driver.find_element(By.ID,"react-burger-menu-btn").click()
sleep(sleep_time)

#by link text
link2  = driver.find_element(By.PARTIAL_LINK_TEXT,"Abo")
link2.click()
sleep(sleep_time+2)

driver.quit()

# checkAvail = driver.find_element(By.CSS_SELECTOR, "button.btn_checkavail")
# checkAvail.click()
#
# sleep(sleep_time)
#
# password = driver.find_element(By.ID,"newpasswd")
# password.send_keys("Shri@9876")
#
# sleep(sleep_time)
#
# passConfirm = driver.find_element(By.ID,"newpasswd1")
# passConfirm.send_keys("Shri@9876")
#
# sleep(sleep_time)
#
# check_box = driver.find_element(By.NAME,"chk_altemaila6445b38")
# check_box.click()


