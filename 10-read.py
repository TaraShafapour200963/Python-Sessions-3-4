count = 0
with open("text.txt", "r", encoding="utf-8") as file:
    while True:
        ch = file.read(1)
        if ch == "":
            break
        print(ch)
        count += 1
print(count)