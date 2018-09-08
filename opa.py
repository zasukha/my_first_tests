class Human:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age
    def say_hello(self):
        print("Hello!!!, " + self.name + self.age)
    def ful_name(self):
        return "Student:" + self.name + "" + self.lname





class Student(Human):
    def __init__(self, name, lname, age):
        self.name = name
        self.lame = lname
        self.age = age
    def say_hello(self):
        print("Hello!!!, " + self.name + self.age)
    def ful_name(self):
        print(self.lname)

student_dima = Student("Dima", "App", "17")
student_sasha = Student("Sasha", "Vas", "19")

student_dima.say_hello()
student_sasha.say_hello()
human1 = Human("Dima", "Last")