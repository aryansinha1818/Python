col = {"name":"Aryan", "age":12}
print(col["name"])
print(col.get('age'))
print(col.get('name'))
print(col)
# would print the values not the keys
print(col.values())
# only keys 
print(col.keys())
print(col.items())
