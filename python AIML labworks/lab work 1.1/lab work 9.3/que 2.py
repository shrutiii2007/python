#multiple inheritance:-
# child inherit from multiple parent classes

class teacher:
    def method1(self):
        return "teacher :- i teach students"
    
class administrator:
    def method2(self):
        return "adminstrator :- i manage school activities"
    
#inherit from multiple parent
class headmaster(teacher, administrator):
    def method3(self):
        return "headmaster :- i lead the school"
    
access = headmaster()
print(access.method1())
print(access.method2())
print(access.method3())