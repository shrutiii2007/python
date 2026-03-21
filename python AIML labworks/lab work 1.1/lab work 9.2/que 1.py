class Car:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} Car Created!")

    def __del__(self):
        print(f"{self.brand} Car Destroyed!")

car1 = Car("Tesla")  
del car1  
car2 = Car("Audi")
del car2
car3 = Car("BMW")
del car3


# output :-
# Tesla Car Created!
# Tesla Car Destroyed!
# Audi Car Created!
# Audi Car Destroyed!
# BMW Car Created!
# BMW Car Destroyed!