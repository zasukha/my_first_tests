print("fuk")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "George"
character_age = 50.25
is_male = False
print("tttt " + character_name + "")
print(str(character_age))

character_name = "Mike"
print("dfg " + character_name + "")
print("df " +  str(character_age) )

phrase = "Giraffe Academy"
print("Giraffe\nAcademy")
print("Giraffe\"Academy\"")
print(phrase + "is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("a"))
print(phrase.replace("Giraffe", "Elephant"))

from math import *
my_num = -5
print(2.00009)
print(-23)
print(3 * (4.5 + 5))
print(30 % 3)
print(my_num)
print(str(my_num) + " is my favorit number")
print(abs(my_num))
print(pow(2, 2))
print(max(6, 7))
print(min(5, 4))
print(round(3.7))
print(floor(3.5))
print(ceil(3.7))
print(sqrt(10))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name.upper() + "!\nYou are " + age + " old,\nand you are so old for IT=(")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
#exn = input("What you gona do?: ")
result = float(num1) + float(num2)
print("\nSummary: " + str(result))

color = input("Enter a clolr: ")
plural_noun = input("Enter a Ploral Noun:  ")
celebrity = input("Enter a celebrity: ")
print("\nRoses are " + color)
print(plural_noun + " are blue")
print("I love" + celebrity)

lucky = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
friends.extend(lucky)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
lucky.sort()
lucky.reverse()
frends2 = friends.copy()
#friends.clear()
#friends.pop()
#friends[1] = "Vasia"
#print(friends[1])
#print(friends)
#print(friends[-1])
#print(friends[1:])
#print(friends[-1:])
#print(friends.index("Kevin"))
#print(friends.count("Jim"))
#print(lucky)
print(frends2)

coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates)

def say_hi(name, age):
   print("Hello " + name + ", you are " + str(age))
print("Top")
say_hi("Mike", "35")
say_hi("Stive", "45")
print("Bottom")


def cube(num):
   return num * num * num
print(cube(4))

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are tall male")
elif is_male and not(is_tall):
    print("You re short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not male and not tall")


def max_num(num1, num2, num3):
   if num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3
print(max_num(3, 56, 170))

you = input("Enter your name: ")
print("\nHello word! I'm " + you.capitalize() + " and I'm Lukky)")

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"chromedriver")
driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("Be QA Today")
driver.find_element_by_name("q").submit()
assert driver.find_element_by_link_text("Be QA Today").is_displayed()
#driver.quit()