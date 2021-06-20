from selenium import webdriver

#path of driver should be specified
driver = webdriver.Chrome(executable_path='C:\\Users\Dell\SeleniumDriver\chromedriver.exe')

driver.get("http://www.facebook.com")

username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
submit = driver.find_element_by_name("login")
username.send_keys("d@mail.ru")
password.send_keys("aaaa")
submit.click()