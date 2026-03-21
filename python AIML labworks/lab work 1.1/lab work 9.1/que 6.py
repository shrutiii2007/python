class person :
    def __init__(self,age):
        self.age = age

    def set_age(self,age):
        if age>0:
            self.age = age
    def get_age(self):
        return self.age
    
person1 = person(20)

print("age",person1.get_age())
person1.set_age(23)
print(" new age",person1.get_age())
