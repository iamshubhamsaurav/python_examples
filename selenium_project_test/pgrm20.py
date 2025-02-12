from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sleep_time = 3

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")

sleep(sleep_time)

#by classname
link1 = driver.find_element(By.CSS_SELECTOR,"p.MuiTypography-root.MuiTypography-body1.makeStyles-link-3.css-1ismtrt-MuiTypography-root")
link1.click()

sleep(sleep_time)

#by id using css selector
link1 = driver.find_element(By.CSS_SELECTOR,"#email")
link1.send_keys("kamath@gmail.com")
sleep(sleep_time)


#by attribute using css selector
link1 = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
link1.send_keys("Kamath@1234")

sleep(sleep_time)

#by class name and attribute
submit = driver.find_element(By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-fullWidth.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-fullWidth.css-1vhaqj4-MuiButtonBase-root-MuiButton-root[tabindex='0']")
submit.click()
sleep(sleep_time+1)
driver.quit()
