import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://login.yahoo.com/?.intl=in")
time.sleep(3)

driver.maximize_window()
time.sleep(3)

#ID
driver.find_element(By.ID,"createacc").click()

#Tag Name
link = driver.find_elements(By.TAG_NAME,"a")
print("\n Number of Links", len(link))

#CSS Selectors Tag Name ,ID
n = driver.find_element(By.CSS_SELECTOR,"input#usernamereg-firstName")
print("\n name is Enabled",n.is_enabled())

#CSS Selectors Tag name ,attributes
ln = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Surname']")
print("Is last name displayed ",ln.is_displayed())

time.sleep(3)
n.send_keys("abc")
time.sleep(2)

ln.send_keys("K")
sleep(2)

driver.find_element(By.NAME,"userId").send_keys("xyzthenameisjohncena")

sleep(3)

driver.find_element(By.NAME,"password").send_keys("ASdf@9876")

sleep(3)
#by classname
driver.find_element(By.CSS_SELECTOR,"button.show-hide-toggle-button[tabindex='-1']").click()
sleep(3)

p = driver.find_element(By.CSS_SELECTOR,"input#usernamereg-password")
print("\n Is password enabled",p.is_enabled())

sleep(3)

p2 = driver.find_element(By.ID,"usernamereg-show-button")
p2.click()
print("\n Is password enabled",p2.is_enabled())

sleep(3)

driver.find_element(By.ID,"usernamereg-month").send_keys("October")
sleep(3)

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Day']").send_keys("12")
sleep(3)

driver.find_element(By.NAME,"yyyy").send_keys("2024")
sleep(3)


signUp = driver.find_element(By.NAME,"signup")
signUp.click()

sleep(3)

driver.quit()

