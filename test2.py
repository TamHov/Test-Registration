from time import sleep

from selenium import webdriver

#path of driver should be specified
driver = webdriver.Chrome(executable_path='C:\\Users\Dell\SeleniumDriver\chromedriver.exe')

driver.get("http://www.facebook.com")

CreateAccountButton = driver.find_element_by_xpath("//*[text()='Create New Account']")
sleep(2)
FirstName = driver.find_element_by_name("firstname")
LastName = driver.find_element_by_name("lastname")
Email = driver.find_element_by_name("reg_email__")
Password = driver.find_element_by_name("reg_passwd__")
Gender = driver.find_element_by_name("sex")
Submit = driver.find_element_by_name("sex")

CreateAccountButton.click()
FirstName.send_keys("testname")
LastName.send_keys("testsurname")
Email.send_keys("test@yopmail.com")
Password.send_keys("aaaaaa")
Gender.click()
Submit.click()