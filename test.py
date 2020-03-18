from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.dogedoge.com/")
element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by="id", value="wedonttrack"))
print(element)