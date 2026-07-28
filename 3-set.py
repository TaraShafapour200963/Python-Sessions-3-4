group1={"علی","زهرا","محمد","رضا"}
group2={"محمد","رضا","سارا","نگار"}
print(group1," ",group2)
group1.add("امیر")
print(group1)
group1.remove("زهرا")
print(group1)
print(len(group1))
print("محمد" in group1)
print(group1.intersection(group2))
print(group1.union(group2))