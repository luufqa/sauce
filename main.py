import time

from selenium import webdriver
from selenium.webdriver.common.by import By

login1 = 'standard_user'
password = 'secret_sauce'
url = "https://www.saucedemo.com/"


def user_auth(log, pas):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.ID, 'user-name').send_keys(log)
    browser.find_element(By.ID, 'password').send_keys(pas)
    time.sleep(2)
    browser.find_element(By.ID, 'login-button').click()
    time.sleep(6)
    if browser.current_url == "https://www.saucedemo.com/":
        res_url = browser.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        return res_url.text
    else:
        return browser.current_url


def check_button(log, pas):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.ID, 'user-name').send_keys(log)
    browser.find_element(By.ID, 'password').send_keys(pas)
    time.sleep(2)
    browser.find_element(By.ID, 'login-button').click()
    time.sleep(6)

    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    browser.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    time.sleep(3)
    res_cart = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")
    return int(res_cart.text)

user_auth(login1, password)
# check_button("error_user", password)
