import numpy as np

#task 4.2

sales = np.array([[10, 20], [15, 25], [12, 18]])
bonuses = np.array([2, 3, 1])

result = sales + bonuses.reshape(3, 1)

print("sales data:-\n",sales)
print("bonuses data:-\n",bonuses)
print("after broadcasting:-\n",result)

#output:-
# sales data:-
#  [[10 20]
#  [15 25]
#  [12 18]]
# bonuses data:-
#  [2 3 1]
# after broadcasting:-
#  [[12 22]
#  [18 28]
#  [13 19]]

#task 4.3

tax_rates = np.array([0.1,0.05])
print("tas rates:-\n",tax_rates)

result = sales * tax_rates
print(result)



