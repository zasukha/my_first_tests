import unittest

from ddt import ddt, file_data
from selenium import webdriver

@ddt
class HW_ZR(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    @file_data('request_data.json')
    def test_login_account_email_validation(self, value):
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.find_element_by_css_selector('a[accesskey="o"]').click()
        self.driver.find_element_by_css_selector('input[name="wpName"]').send_keys('zas_rv')
        self.driver.find_element_by_css_selector('input[id="wpPassword1"]').send_keys('forester777')
        self.driver.find_element_by_id("wpLoginAttempt").click()

        #self.driver.find_element_by_css_selector('a[aria-label="Close"]').click()

        self.driver.find_element_by_css_selector('input[id="searchInput"]').send_keys(value)
        self.driver.find_element_by_css_selector('input[ id="searchButton"]').click()
        self.driver.find_element_by_css_selector('a[title="Ukraine"]').click()
        self.assertTrue(self.driver.find_element_by_css_selector('img[alt="Flag of Ukraine"]').is_displayed())

    def tearDown(self):
        self.driver.quit()