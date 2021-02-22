from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
link = "http://suninjuly.github.io/wait2.html"

"""
title_is 
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
"""
try:


    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    driver.get(link)
    button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()
    message = driver.find_element(By.ID,"verify_message")

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    assert "successful" in message.text
    driver.quit()

