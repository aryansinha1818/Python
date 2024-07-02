countries = ("Spain", "Italy", "India", "England", "Germany")
t1 = list(countries)
t1.append("Hello world!")
t1[0] = "Aryan Sinha"
t1.pop(3)
countries = tuple(t1)
print(countries)

t2 = (1,2,3,4,5)
print(t2+countries)