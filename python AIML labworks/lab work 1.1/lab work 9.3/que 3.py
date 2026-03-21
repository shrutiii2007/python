class Grandparent:
    def grand_method(self):
        return "Grandparent method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent method"

class Child(Parent):
    def child_method(self):
        return "Child method"

c = Child()
print(c.grand_method())  # Output: Grandparent method
print(c.parent_method())  # Output: Parent method
print(c.child_method())  # Output: Child method



