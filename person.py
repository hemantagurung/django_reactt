class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


class Student(Person):
    def __init__(self, name, age, major, roll, marks):
        super().__init__(name,age) #initializing ihertited attributes 
        self.major = major 
        self.roll = roll
        self.marks = marks

    def display_student_info(self):
        self.display_info()
        print (f"major: {self.major}")
        print (f"roll: {self.roll}")
        print (f"marks: {self.marks}")

Student = Student("ram", 30, "BBA", "a20", 99)
Student.display_student_info()


              
        