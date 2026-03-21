
print("Enter marks for three subjects out of 100:")

sub1 = int(input("Marks in English: "))
sub2 = int(input("Marks in Maths: "))
sub3 = int(input("Marks in Science: "))


print("Student Marksheet")
print("English Marks:", sub1)
print("Maths Marks  :", sub2)
print("Science Marks:", sub3)


total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F (Fail)"


print("Total Marks  :", total, "/ 300")
print("Percentage   :", round(percentage), "%")
print("Grade        :", grade)


