def integer(n):
    return list(range(n))
def square(n):
     return [i * i for i in range(n)]  #1*1=1 2*2=4 3*3=9 4*4=16

intlist = integer(5)
print("Integer list:", intlist)

squlist = square(5)
print("Square list:", squlist)

# output:-
# Integer list: [0, 1, 2, 3, 4]
# Square list: [0, 1, 4, 9, 16]