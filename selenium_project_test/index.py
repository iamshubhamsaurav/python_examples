from selenium import webdriver
from selenium.webdriver.common.by import By

import time



driver = webdriver.Chrome()




driver.get("http://localhost:3000/dashboard/676d3fc7f141389d32bea4b2")

title = driver.title

driver.maximize_window()

driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/button[1]").click()
# time.sleep(5000)


driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]").send_keys("Dummy title")

driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/textarea[1]").send_keys("Dummy text fpr the body")



driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()


time.sleep(5000)