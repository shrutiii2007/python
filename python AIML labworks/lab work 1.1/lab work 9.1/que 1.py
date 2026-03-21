class Person:
    def __init__(self, name, age):
        self.name = name      
        self.age = age        

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("karti", 20)
p2 = Person("Shruti", 18)

p1.display()
p2.display()

# output:- Name: krati
# Age: 20
# Name: Shruti
# Age: 18