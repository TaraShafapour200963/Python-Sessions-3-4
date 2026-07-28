with open("students.txt","w",encoding="UTF-8") as file:
    file.write("tara\n")
    file.write("mobina\n")
    file.write("sara\n")
with open("students.txt","r",encoding="UTF-8") as file:
    data=file.read()
    print(data)