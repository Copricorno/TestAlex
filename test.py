from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def reg():
    driver.get("https://extremstyle.ua/ru/site/signup")

    FIO = driver.find_element_by_id("signupform-username")
    Pass = driver.find_element_by_id("signupform-password")
    RePass = driver.find_element_by_id("signupform-password_repeat")
    Your_Email = driver.find_element_by_id("signupform-email")

    FIO.send_keys("test-user")
    Pass.send_keys("1234567890Aa")
    RePass.send_keys("1234567890Aa")
    Your_Email.send_keys("Copricorno@ukr.net",Keys.ENTER)


new = reg() #1234567890


