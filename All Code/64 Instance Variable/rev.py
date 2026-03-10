class Employee:
    companyName = "Zomato"
    noOfPeople = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.12
        Employee.noOfPeople += 1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount is {self.raise_amount} and the total employees are {self.noOfPeople}")

# class variable and instance variable, it first looks in the instance variable if it is there then that is the result & if not then the class variable 
emp1 = Employee("Aryan")
emp1.showDetails()
emp2 = Employee("Rishabh")
emp2.showDetails()

emp1.raise_amount = 500
print(emp1.raise_amount)
print(emp2.raise_amount)