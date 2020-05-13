x = { "a":"b","c":"d","e":"f "}
x.copy()
print(x)

z = ('q', 'w', 'e')
y = 0
G = dict.fromkeys(z,y)
print(G)

print(x.get("c"))

print(x.items())

print(x.keys())

x.update({"r":"p"})
print(x)

x.pop("r")
print(x)

x.clear()
print(x)