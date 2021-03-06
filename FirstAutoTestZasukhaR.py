"""
This is test for login, how wiki search requests for Ukraine and logout flow. Request_data.json is need to run this test.
"""

import unittest

from ddt import ddt, file_data
from selenium import webdriver

user_name = "zas_rv"  # input your login
password = "forester777"  # input your password


@ddt
class FirstAutoTestZasukhaR(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    @file_data('request_data.json')
    def test_login_search_logout_flow(self, value):
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.assertTrue(self.driver.find_element_by_css_selector('a[class="mw-wiki-logo"]').is_displayed())
        self.driver.find_element_by_css_selector('[id="pt-login"]').click()

        self.driver.find_element_by_css_selector('input[name="wpName"]').send_keys(user_name)
        self.driver.find_element_by_css_selector('input[id="wpPassword1"]').send_keys(password)
        self.driver.find_element_by_css_selector('button[id="wpLoginAttempt"]').click()
        self.assertTrue(self.driver.find_element_by_css_selector('li[id="pt-logout"]').is_displayed())

        self.driver.find_element_by_css_selector('input[id="searchInput"]').send_keys(value)
        self.driver.find_element_by_css_selector('input[id="searchButton"]').click()
        self.driver.find_element_by_css_selector('a[title="Ukraine"]').click()
        self.assertTrue(self.driver.find_element_by_css_selector('img[alt="Flag of Ukraine"]').is_displayed())
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="/wiki/Shche_ne_vmerla_Ukraina"]').is_displayed())

        self.driver.find_element_by_css_selector('li[id="pt-logout"]').click()
        self.assertTrue(self.driver.find_element_by_css_selector('li[id="ca-nstab-special"]').is_displayed())

    def tearDown(self):
        self.driver.quit()
