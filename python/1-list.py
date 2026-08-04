shopping=["برنج","تخم مرغ","شیر","نان"]
print(shopping)
shopping.append("ماست")
print(shopping)
shopping.remove("شیر")
print(shopping)
print(len(shopping))
print("برنج" in shopping)
shopping.sort()
print(shopping)
user=input()
if user in shopping:
    shopping.remove(user)
    print(shopping)
else:
    print("وجود ندارد")