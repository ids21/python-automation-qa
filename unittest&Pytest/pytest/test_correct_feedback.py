import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

links_data = """https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1"""
links = links_data.split("\n")


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    def resource_teardown():
        driver.quit()

    request.addfinalizer(resource_teardown)
    return driver

@pytest.mark.parametrize("link",links)
class TestFeedback:
    def test_click(self, link, setup):
        answer = str(math.log(int(time.time())))
        setup.get(link)
        textarea = WebDriverWait(setup, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[required]"))
        )
        textarea.send_keys(answer)

        button = setup.find_element_by_css_selector(".submit-submission")
        button.click()

        banner = WebDriverWait(setup, 12).until(
            EC.presence_of_element_located((By.TAG_NAME, "pre"))
        )
        result = banner.text

        assert "Correct!" == result, "Result is not as expected"



