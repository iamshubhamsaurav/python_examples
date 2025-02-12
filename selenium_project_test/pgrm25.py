
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://login.yahoo.com/?.intl=in")

time.sleep(3)
driver.maximize_window()
time.sleep(3)
# is_selected
checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[3]/div[1]/span/input")
time.sleep(2)
#conditional command
print("Check box Stay signed in is selected ", checkbox.is_selected())

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[3]/div[1]/span/label").click()
time.sleep(3)

checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[3]/div[1]/span/input")
#conditional command is selected
print("After click checkbox status ", checkbox.is_selected())

#navigational command
driver.refresh()
time.sleep(5)
#ID
driver.find_element(By.ID, "createacc").click()
#Tag anme
link =driver.find_elements(By.TAG_NAME, "a")
print("Number of links", len(link))
# CSS selectors
n=driver.find_element(By.CSS_SELECTOR, "input#usernamereg-firstName")
print("name is Enabled",n.is_enabled())
ln = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Surname']")
print("Is last name displayed",ln.is_displayed())
n.send_keys("abc")
time.sleep(2)
ln.send_keys("K")

time.sleep(2)
driver.find_element(By.NAME, "userId").send_keys("xyz")
driver.find_element(By.NAME, "password").send_keys("xyz")
driver.find_element(By.CSS_SELECTOR, "button.show-hide-toggle-button[tabindex='-1']").click()
p = driver.find_element(By.CSS_SELECTOR, "input#usernamereg-password")
print("Is password is enabled", p.is_enabled())
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign").click()
time.sleep(2)
#navigation
driver.forward()
time.sleep(2)
#navigation
driver.back()
time.sleep(2)
#navigation
driver.close()





























