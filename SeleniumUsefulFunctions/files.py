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
link = "http://suninjuly.github.io/file_input.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

    curr_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curr_path,"file.txt")

    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    driver.find_element(By.NAME,"firstname").send_keys("ALeksandr")
    driver.find_element(By.NAME, "lastname").send_keys("kek")
    driver.find_element(By.NAME, "email").send_keys("sf@dfs.ru")
    driver.find_element(By.CSS_SELECTOR,"[type='file']").send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    driver.quit()




assert True