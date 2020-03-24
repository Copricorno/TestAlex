from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def driverFF(url):
    driver = webdriver.Firefox()
    driver.get(f"{url}")

def find_write(element,write):
    global driver
    a = driver.find_element_by_id(f"{element}")
    b = a.send_keys(f"{write}")


def press_bottom(bottom):
    b = driver.find_element_by_name(f"{bottom}")
    var = b.click
    return var

driverFF("https://extremstyle.ua/ru/site/signup")
find_write("signupform-username","test-use")