a = open("text.txt", "w")
a.write("text")
a.close()

a = open("text.txt", "r")
print(a.read())
 