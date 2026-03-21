class info:
    print("missing self beacuse of that attribute is not linked to the instance")
    def __init__(name, surname):
       
        name = name
        surname = surname

info_person = info("shruti","Bhawsar")
print(info_person.name)

# error will come 