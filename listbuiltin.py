x = ["a", "b", "c"]
y = ["x", "y", "z"]

x.append("d")
print(x)

print(x.count("a"))

x.extend(y)
print(x)

print(x.index("c"))

x.insert(2,"e")
print(x)

x.pop(2)
print(x)

x.remove("y")
print(x)

x.reverse()
print(x)

x.sort()
print(x)
