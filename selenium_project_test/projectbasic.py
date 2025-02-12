from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sleep_time = 3

driver = webdriver.Chrome()

driver.get("http://localhost:3000/adminlogin")

sleep(sleep_time)

name  = driver.find_element(By.ID,"email")
name.send_keys("admin")

sleep(sleep_time)

mail = driver.find_element(By.NAME,"password")
mail.send_keys("Admin123")

sleep(sleep_time)


button = driver.find_element(By.ID,"submit")

button.click()


sleep(sleep_time+4)
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

submitButton = driver.find_element(By.ID,"submit")

submitButton.click()


sleep(sleep_time+2)

driver.quit()
