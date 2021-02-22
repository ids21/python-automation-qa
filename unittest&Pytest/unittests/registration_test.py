import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


class TestRegistration(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')

    def test_is_equal_labels_v1(self):
        cases = ['First name*','Last name*','Email*']
        link = "http://suninjuly.github.io/registration1.html"

        driver = self.driver
        driver.get(link)
        first_name_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.first_class label")
        last_name_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.second_class label")
        email_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.third_class label")
        parse_data = [first_name_text.text, last_name_text.text, email_text.text]

        with self.subTest(case = cases):
            self.assertEqual(cases,parse_data)


    def test_is_equal_labels_v2(self):
        cases = ['First name*','Last name*','Email*']
        link = "http://suninjuly.github.io/registration2.html"
        driver = self.driver
        driver.get(link)
        first_name_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.first_class label")
        email_text = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.third_class label")
        parse_data = [first_name_text.text,email_text.text]

        with self.subTest(case = cases):
            self.assertEqual(cases,parse_data)

    def tearDown(self):
        self.driver.quit()


def reg_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRegistration('test_is_equal_labels_v1'))
    suite.addTest(TestRegistration('test_is_equal_labels_v2'))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    test_suite = reg_test_suite()
    runner.run(test_suite)