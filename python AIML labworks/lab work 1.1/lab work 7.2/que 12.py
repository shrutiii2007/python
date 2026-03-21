x = 0

def initialize(a):
    global x
    x = a
    print("Initialize value:", x)

def increment(b):
    global x
    x += b
    print("increment:", x)

initialize(10)  
increment(5)     
increment(3)    

# output is :-
# Initialize value: 10
# increment: 15
# increment: 18