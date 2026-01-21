from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
from time import sleep


with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    PRICE_LOCATOR = ('id', 'price')
    BUTTON_LOCATOR = ('id', 'book')
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((PRICE_LOCATOR), '$100'))
    button = browser.find_element(*BUTTON_LOCATOR)
    button.click()
    x_element = browser.find_element('id', 'input_value')
    x = int(x_element.text)
    y = log(abs(12*sin(x)))
    browser.find_element('id', 'answer').send_keys(str(y))
    browser.find_element('xpath', '//button[@type="submit"]').click()
    print(browser.switch_to.alert.text.split()[-1])
    sleep(1)
    browser.switch_to.alert.accept()
    sleep(1)