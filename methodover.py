class Animal:
    def speak(self):
        print("i am an animal. i make the sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        return "woof!"

class Cat (Animal):
    def speak(self):
        return "MEow!"


animals = [Dog(), Cat()]
for animal in animals:
    print (animal.speak())





