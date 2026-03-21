def cube(number):

  return number ** 3

def listing(numbers, operation):

  list = []
  for num in numbers:
    list.append(operation(num))
    # operation(num) calls krega cube(1) ko joki returns krega 1³ = 1.
    # result (1) appended ho jayega list me.
    # yhi process repeat hogi
  return list

my_num = [1, 2, 3, 4, 5]
cubed= listing(my_num, cube)

print(f"Original numbers: {my_num}")
print(f"Cubed numbers: {cubed}")

# output:-
# Original numbers: [1, 2, 3, 4, 5]
# Cubed numbers: [1, 8, 27, 64, 125]
# (1 * 1 * 1 = 1)
# (2 * 2 * 2 = 8)
# (3 * 3 * 3 = 27)
# (4 * 4 * 4 = 64)
# (5 * 5 * 5 = 125) 