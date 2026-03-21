class animal:
    def method1(self):
        return "animals"

class dog(animal):
    def method2(self):
        return "dog"

class cat(animal):
    def method3(self):
        return "cat"

animal1 = dog()
animal2 = cat()

print(animal1.method1())   
print(animal1.method2())   

print(animal2.method1())  
print(animal2.method3())  

#output :-
# animals
# dog
# animals
# cat