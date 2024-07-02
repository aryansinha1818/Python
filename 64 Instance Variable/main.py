class Class:
    def __init__(self,section):
        self.section = section 
    def question(self):
        print(f"The section is {self.section}")

A10 = Class("D")
print(A10.section)
A10.question()
Class.question(A10)