import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
link = "http://suninjuly.github.io/math.html"
import math
import numpy as np

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    x = driver.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x.text
    y = calc(x)
    field = driver.find_element(By.CSS_SELECTOR,"#answer.form-control")
    field.send_keys(y)
    bot = driver.find_element(By.CSS_SELECTOR, ".form-check-input#robotCheckBox")
    bot.click()
    RadioButton = driver.find_element(By.CSS_SELECTOR, "[for = robotsRule]")
    RadioButton.click()

    button = driver.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()



except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    driver.quit()