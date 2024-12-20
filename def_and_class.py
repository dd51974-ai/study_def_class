def greet(name):
    return f"hello, {name}"


print(greet("Emma"))

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"
my_cars = []
my_cars.append(Car("Toyota", "Carolla", 2020))
my_cars.append(Car("Toyota", "Hilux", 1989))
my_cars.append(Car("Toyota", "Supra", 1991))

for car in my_cars:
    print(car.description())