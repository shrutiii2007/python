#1
i=10
while i<=10:
     num=int(input("Enter your number:"))
     if num==0:
         break


#2
             
i=1
for i in range(1,11):
    print(i*i)
    i=i+1


#3

i=1
while i<=50:
    if i%2==0:
        print(i)
    i=i+1


#4

i=1
for i in range(1,21):
    if i%2!=0:
        print(i)
        i=i+1

    
#5

for i in range(5,51,5):
        print(i)


#6

for i in range(10,0,-1):
    print(i)

#7
Name="PYTHON"
vowels = "AEIOUaeiou"
for Name in Name:
    if Name in vowels:
        continue
    print(Name)
