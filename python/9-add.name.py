user=input("enter name:")
with open("students.txt","a",encoding="UTF-8") as file:
    file.write(user+"\n")
with open("students.txt","r",encoding="UTF-8") as file:
    data=file.read()
    print(data)
with open("students.txt","r",encoding="UTF-8") as file:
    count = 1
    for name in file:
        print(count, "-", name.strip())
        count += 1