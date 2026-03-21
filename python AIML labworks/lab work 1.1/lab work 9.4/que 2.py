class shape:
    def area(self):
        return 0
    
class circle(shape):
    def area(self):
        return "area of circle"
    
class rectangle(shape):
    def area(self):
        return "area of rectangle"
    
c=circle()
r=rectangle()

print(c.area())
print(r.area())


# output:-
# area of circle
# area of rectangle