import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r"chromedriver")
driver.implicitly_wait(10)

driver.get("https://www.ukr.net/")
driver.find_element_by_name("Login").send_keys("zas_rv")
driver.find_element_by_name("Password").send_keys("opelvectra777")
driver.find_element_by_name("level").click()
driver.find_element_by_css_selector('div.login-block__submit button').click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.l')))
driver.find_element_by_css_selector('a.l').click()
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.xpath, '/html/body/div[2]/div[4]/div[4]/div/div[2]/ul/li[6]/a')))
##driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[2]/ul/li[6]/a').click()
#element = wait.until(EC.element_to_be_clickable((By.xpath, '/html/body/div[2]/div[4]/div[4]/div/div[2]/ul/li[6]/a')))
driver.find_element_by_partial_link_text('g/logout').click()