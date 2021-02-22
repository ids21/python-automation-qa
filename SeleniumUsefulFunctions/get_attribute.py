import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
link = "http://suninjuly.github.io/get_attribute.html"
import math
import numpy as np

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    x_ = driver.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_.get_attribute("valuex")
    y = calc(x)
    print(y)
    field = driver.find_element(By.CSS_SELECTOR,"#answer")
    field.send_keys(y)
    bot = driver.find_element(By.CSS_SELECTOR, ".check-input#robotCheckBox")
    bot.click()
    RadioButton = driver.find_element(By.CSS_SELECTOR, ".check-input#robotsRule")
    RadioButton.click()

    button = driver.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()



except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    driver.quit()