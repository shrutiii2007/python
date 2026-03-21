class employee:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} Employee Created!")

    def __del__(self):
        print(f"{self.name} employee delete. Goodbye !")


e1 = employee("shruti")   
del e1

# output:-
# shruti Employee Created!
# shruti employee delete. Goodbye !