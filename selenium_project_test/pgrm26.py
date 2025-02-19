from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
sleep(3)

#find_element to locate one element
searchBox = driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
searchBox.send_keys("Mobile")
sleep(5)

#use find_element to find multiple elemets
footerlinks = driver.find_element(By.XPATH,"//div[@class='footer'] //a")
print(footerlinks.text)

#use find_element to find multiple element and length
footerlinks = driver.find_element(By.XPATH,"//div[@class='footer'] //a")

#find_elements to loacte single element
element = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print("Length  ",len(element))

element[0].send_keys("Apple MacBook Pro13-inch")

sleep(2)
#locate multiple elements
element = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(element))


login_element = driver.find_elements(By.LINK_TEXT, "Log")
print("Elements returened :", len(login_element))
# login_element.click()
sleep(2)
driver.close()
