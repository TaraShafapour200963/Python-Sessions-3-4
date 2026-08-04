book={
    "title":"python",
    "author":"ahmadi",
    "publisher":"danesh",
    "year":2024,
    "pages":350
}
print(book.items())
print(book["title"])
print(len(book))
book["year"]=2025
print(book)
book["price"]=450000
print(book)
del book["publisher"]
print(book)
print(book.keys())
print(book.values())
for key,value in book.items():
      print(key,":",value," ")

student={
      "نام":"تارا",
      "نام خانوادگی":"شفاپور",
      "سن":16,
      "رشته":"شبکه و نرم افزار",
      "معدل":"20"
}
sortedstudent= dict(sorted(student.items()))
print(sortedstudent)