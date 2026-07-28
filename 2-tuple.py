students=("رضا","علی","محمد","زهرا","علی")
print(students)
print(len(students))
print(students[2])
print("محمد" in students)
print(students.count("علی"))
print(students.index("رضا"))
print(students[:2])
for s in students:
    print(s," ")
studentlist=list(students)
studentlist.append("سارا")
print(studentlist)
user=input()
if user in students:
    print(students.index(user))
else:
    print("وجود ندارد")