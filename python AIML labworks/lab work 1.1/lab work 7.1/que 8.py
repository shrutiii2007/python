def filter_data(*value):
    string =[]
    number =[]

    for a in value:
        if isinstance (a,str):
            string.append(a)
        elif isinstance (a,(int,float)):
            number.append(a)

    return tuple(string),tuple(number)

print(filter_data("a",22,"shruti",45.76 , True ,68 ))

# output:-
# (('a', 'shruti'), (22, 45.76, True, 68))