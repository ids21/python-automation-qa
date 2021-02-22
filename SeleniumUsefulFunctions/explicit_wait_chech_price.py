from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    driver.find_element(By.ID,"book").click()
    x = driver.execute_script("return x = document.getElementById('input_value');x.scrollIntoView(true);")
    y = calc(x.text)
    driver.execute_script("return x = document.getElementById('answer');x.scrollIntoView(true);").send_keys(y)
    button2 = driver.find_element(By.ID,"solve")
    driver.execute_script("return arguments[0].scrollIntoView", button2)
    button2.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    driver.quit()

