import pandas as pd

#task 2.1
fruits = ['apple', 'banana', 'cherry', 'date']
series = pd.Series(fruits)
print(series)

#output:-
# 0     apple
# 1    banana
# 2    cherry
# 3      date
# dtype: object

print()

#task 2.2
color_list = ['red','green','blue']
color_num = ['color1','color2','color3']
series = pd.Series(color_list, index=color_num)
print(series)

#output:-
# color1      red
# color2    green
# color3     blue
# dtype: object

print()

#task 2.3
fruit = fruits[1]
print("fruits index num :-",fruit)

#output:-
# fruits index num :- banana

color = series['color2']
print("color name :-",color)

#output:-
# color name :- green

