from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="function")
def resource_setup(request):
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    def resource_teardown():
        driver.quit()
    request.addfinalizer(resource_teardown)
    return driver

def test_is_equal_labels_v1(resource_setup):
    cases = ['First name*','Last name*','Email*']
    link = "http://suninjuly.github.io/registration1.html"
    driver = resource_setup
    driver.get(link)
    first_name_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.first_class label")
    last_name_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.second_class label")
    email_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.third_class label")
    assert cases[0] == first_name_text.text
    assert cases[1] == last_name_text.text
    assert cases[2] == email_text.text


def test_is_equal_labels_v2(resource_setup):
    cases = ['First name*','Last name*','Email*']
    link = "http://suninjuly.github.io/registration2.html"
    driver = resource_setup
    driver.get(link)
    first_name_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.first_class label")
    email_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.third_class label")
    assert cases[0] == first_name_text.text
    assert cases[1] == email_text.text



