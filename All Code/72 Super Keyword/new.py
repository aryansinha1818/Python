class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

"""class Programmer:
    def __init__(self,name, id,lang):
        self.name = name
        self.id = id
        self.lang = lang"""
class Programmer(Employee):
    def __init__(self,name, id,lang):
        super().__init__(name,id)
        self.lang = lang

rohan = Employee("Ritik ", "420")
print(rohan.name)
q1 = Programmer("Aryan", 12,"C++")
print(q1.name)
print(q1.id)
print(q1.lang)
