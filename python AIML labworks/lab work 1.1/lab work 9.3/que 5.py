class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()  # Calls A's show()
        print("Class B")

class C(B):
    def show(self):
        super().show()  # Calls B's show()
        print("Class C")

obj = C()
obj.show()