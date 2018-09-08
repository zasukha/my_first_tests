from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"chromedriver")
driver.implicitly_wait(10)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.find_element_by_name('search').send_keys('it')
driver.find_element_by_name('go').click()
driver.find_element_by_partial_link_text('Information_Technology').click()
