class Parent:
    def display(self):
        return "Parent class method"

class Child(Parent):
    pass

c = Child()
print(c.display())
