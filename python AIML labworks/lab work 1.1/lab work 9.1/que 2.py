class counter:
    def __init__(self):
        self.count = 0
      
    def increment(self):
        self.count += 1
      
    def ans(self):
        print("final count:-",self.count)

a=counter()
a.increment()
a.increment()
a.increment()
a.increment()
a.ans()

# output:-
# final count:- 4