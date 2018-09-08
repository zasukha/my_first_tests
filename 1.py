"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"chromedriver")
driver.implicitly_wait(5)

driver.get("https://www.ukr.net/")
driver.find_element_by_name("Login").send_keys("zas_rv")
driver.find_element_by_name("Password").send_keys("opelvectra777")
driver.find_element_by_name("level").click()
driver.find_element_by_css_selector('div.login-block__submit button').click()
driver.find_element_by_css_selector('a.l').click()

#driver.find_element_by_css_selector('li.login-block__email').click()
#driver.find_element_by_name("q").submit()
#assert driver.find_element_by_link_text("Be QA Today").is_displayed()
#driver.quit()
#driver.find_element_by_class_name("login-block__submit-but").click()  інший спосіцб 9 рядка


def cube(number):
    print("Number: " + str(number))

cube(23)
cube(43)
cube(1234)


def cube(number):
    return number * number * number

result = cube(3)
result2 = cube(4)
print(result)
print(result2)



def add(a, b):
    return a + b

result = add(3, 6)
print(result)
"""



class Human:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    def full_name(self):
        return self.name + " " + self.last_name

class Student(Human):
    def __init__(self, name, last_name, score):
        self.name = name
        self.last_name = last_name
        self.score = score
    def full_name(self):
        return "Student: " + self.name + " " + self.last_name
    def say_hello(self):
        print("Hello, " + self.name)

human1 = Human("Dima", "Last Name")
student_dima = Student("Dima", "Student", 34)
print(student_dima.full_name())