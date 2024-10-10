import json

class BaseClass:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)

class Student(BaseClass):
    def __init__(self, roll_no, name, batch, car):
        self.roll_no = roll_no
        self.name = name
        self.batch = batch
        self.car = car

    def print_name(self):
        print("YO,",self.name)

    def print_car(self):
        print("NAME OF STUDENT: ", self.name)
        print("CAR:", self.car.getFields())

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

class Car(BaseClass):
    def __init__(self, brand, name, year):
        self.brand = brand
        self.name = name
        self.year = year

    def getFields(self):
        return(self.brand, self.name, self.year)

honda = Car("Honda", "city", "2005")
s1 = Student("85", "Geomina", "2005", honda)
# s1.print_car()

print(s1.toJSON())


# honda.print_name()
# s1.print_name()
# c2= Car("BMW", "3 Series", "2009")
# print(s1)
# print(c1)

s = "MIKE"
