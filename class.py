
#this is class to object

class Car:
    def __init__(self,make,model,year):
          self.make = make
          self.model = model
          self.year = year


def description(self):
	return f"year is{self.year} {self.make}{self.model}"
	

my_car = Car("toyata", "camary", 2001)
# print(my_car.description())

print(dir(my_car))



#Inheritence
		
		