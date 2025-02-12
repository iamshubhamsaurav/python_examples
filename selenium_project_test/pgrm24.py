# Experiment on selected website

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome() #application clomma

# get the webpage
driver.get("https://www.saucedemo.com/")   # Application command
driver.maximize_window()                                # Browser command

# get title of the application
print ("\n Title is :",driver.title)
sleep(3)
# To get URL of the current page

print("\n URL is : ",driver.current_url)
sleep(3)
#Get Source code of the page
print("\n Source code is :", driver.page_source)
sleep(3)
driver.close() 

