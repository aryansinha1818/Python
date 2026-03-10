# class Calculator:
#     def __init(self, version:int):
#         self.version = version
    
#     def description(self):
#         print(f"Currently running Calculation on version: {self.version}")

class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
    
e1 = Employee()
e1.name = "Aryan Sinha"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
print(e1.company)
