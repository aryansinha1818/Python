class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Class methods used as alternative constructor  
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e = Employee("Michelle",12000)
print(e.name)
print(e.salary)

str = "Pankaj-14000"
e1 = Employee(str.split("-")[0],str.split("-")[1])
print(e1.name)
print(e1.salary)

str2 = "Rahul-500000"
e2 = Employee.fromStr(str2)
print(e2.name)
print(e2.salary)
