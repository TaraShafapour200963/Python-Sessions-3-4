library={
    "books":[
        ("python","ahmadi",2023),
        ("network","karimi",2022),
        ("python","ahmadi",2023)
    ],
    "subject":{"python","network","programming"}
}
print(len(library["books"]))
print(library["books"][0])
print(library["books"][0][0])
library["books"].append(("linux","rahimi",2024))
print(library["books"])
library["subject"].add(("security"))
print(library["subject"])
print(len(library["subject"]))
for book in library["books"]:
    print("عنوان :", book[0])
    print("نویسنده :", book[1])
    print("سال :", book[2])
    print("------------------")
for s in library["subject"]:
    print(s," ")
print("python" in library["subject"])
print(library)
library["manager"]="ali ahmadi"
print(library)