class Math:
    def add(self, a, b=0, c=0):
        return a + b + c  

m = Math()

print(m.add(5))       
print(m.add(5, 10))   
print(m.add(5, 10, 15)) 

class variable:
    def add(self,name,surname,nickname):
        return name + surname + nickname

v = variable()

print(v.add("shruti","",""))
print(v.add("shruti","bhawsar",""))
print(v.add("shruti","bhawsar","sonu"))

# #output:-
# 5
# 15
# 30
# shruti
# shrutibhawsar
# shrutibhawsarsonu