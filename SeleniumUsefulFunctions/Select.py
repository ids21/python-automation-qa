import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
link = "http://suninjuly.github.io/selects1.html"
import math
import numpy as np
from functools import reduce
try:
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    sum = reduce(lambda x,y:int(x.text)+int(y.text),driver.find_elements(By.CSS_SELECTOR,".container .nowrap:nth-child(even)"))
    select = Select(driver.find_element(By.CSS_SELECTOR,"#dropdown.custom-select"))
    print(sum)
    select.select_by_visible_text(str(sum))
    button = driver.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()



except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    driver.quit()