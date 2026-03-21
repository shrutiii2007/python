#w mode
file = open("demo.txt","w")
file.write("written using w mode.\n")
file.close()

#r mode
file = open("demo.txt","r")
print(file.read())
file.close()

#a mode
file = open("demo.txt","a")
file.write("appended using a mode.\n")
file.close()

#r+ mode
file = open("demo.txt","r+")
print(file.read())
file.write("added using r+ mode.\n")
file.close()

#w+ mode
file = open("demo.txt","w+")
file.write("written using w+ mode.\n")
file.seek(0)
print(file.read())
file.close()

#a+ mode
file = open("demo.txt","a+")
file.write("added using a+ mode.\n")
file.seek(0)
print(file.read())
file.close()