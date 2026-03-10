class Adder:
    def __init__(self, addend):
        self.addend = addend
    
    def __call__(self,value):
        return value+self.addend

add_five = Adder(5)
res = add_five(10)
print(res)

a1 = Adder(100)
print(a1(20))
"""
When to Use __call__
Function-like Objects:

When you want to create objects that can be used as functions.
Example: Implementing mathematical functions, callable configurations, etc.
Design Patterns:

Implementing design patterns like the Command pattern where objects represent actions or commands that can be called.
Decorators:

Creating callable classes that can act as decorators, allowing more complex stateful behavior than functions."""