class Student:
    def __init__(self, name, roll, marks):
        self.name = name      
        self.roll = roll        
        self.marks = marks      

    def show_details(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.marks)

    def update_marks(self, new_marks):
        self.marks = new_marks
        print("Marks update:", self.marks)

s1 = Student("Rahul", 23, 88)

s1.show_details()      
s1.update_marks(95)   
s1.show_details()      
