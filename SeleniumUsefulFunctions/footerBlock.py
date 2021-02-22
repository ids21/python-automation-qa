import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import math
import numpy as np
from functools import reduce
link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    x = driver.find_element(By.CSS_SELECTOR,"span#input_value ").text
    y = calc(x)
    driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys(y)
    driver.execute_script("window.scrollBy(0,200);")
    driver.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']").click()
    driver.find_element(By.CSS_SELECTOR,"[for='robotsRule']").click()
    driver.find_element(By.TAG_NAME,"button").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    driver.quit()




assert True