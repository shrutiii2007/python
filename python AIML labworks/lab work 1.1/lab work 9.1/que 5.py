class Account:
    def __init__(self, bal, acc):
        self.__balance = bal       # private __  Balance access nhi kr skte kyuki __private
        self.account_no = acc

    def debit(self, amount):
        print("Total balance =", self.get_balance())
        self.__balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.__balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())    #Method display balance krne ke liye

    def get_balance(self):
        return self.__balance      # display method
        

# object creation
acc1 = Account(10000, 12345)
acc1.debit(1000)                      #Methods deposit & withdraw krne ke liye
acc1.credit(500)       
acc1.credit(40000)


# output:-
# Total balance = 10000
# Rs. 1000 was debited
# Total balance = 9000
# Rs. 500 was credited
# Total balance = 9500
# Rs. 40000 was credited
# Total balance = 49500


