import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import math
import numpy as np
from functools import reduce
import os
link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:


    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    y=calc(driver.find_element(By.CSS_SELECTOR,"span#input_value").text)

    driver.find_element(By.CSS_SELECTOR,".form-control#answer").send_keys(y)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    driver.quit()




assert True