"""
In Python, str(e) and repr(e) are used to get the string representations of the object e by calling the __str__ and __repr__ methods, respectively. These methods are special or "dunder" (double underscore) methods that you can define in your class to control how your objects are represented as strings.

Concepts: __str__ and __repr__
__str__ Method:

The __str__ method is used to define the "informal" or nicely printable string representation of an object.
This method is called by the str() built-in function and by the print function when you print an object.
The goal of __str__ is to return a readable and user-friendly string.
__repr__ Method:

The __repr__ method is used to define the "official" string representation of an object.
This method is called by the repr() built-in function and by the interactive interpreter when you inspect an object.
The goal of __repr__ is to return a string that would allow someone to recreate the object, ideally by passing it to eval().
Example with Employee Class
Let's define an Employee class with __str__ and __repr__ methods:

python

class Employee:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Employee name is {self.name}"
    
    def __repr__(self):
        return f"Employee('{self.name}')"

e = Employee("Harry")
print(str(e))  # Calls e.__str__()
print(repr(e)) # Calls e.__repr__()
Explanation
Creating an Instance:

python
Copy code
e = Employee("Harry")
An instance e of the Employee class is created with the name "Harry".
Calling str(e):

python
Copy code
print(str(e))
This calls the __str__ method of the Employee class.
__str__ returns "Employee name is Harry", which is printed.
Calling repr(e):

python
Copy code
print(repr(e))
This calls the __repr__ method of the Employee class.
__repr__ returns "Employee('Harry')", which is printed.
Why Not e.str() or e.str?
Special Methods (__str__ and __repr__): These methods are designed to be used with the str() and repr() functions. They are part of Python's data model and provide a standardized way to define string representations for objects.
Consistency: Using str(e) and repr(e) ensures consistency across different classes and objects. When you define __str__ and __repr__, Python knows how to handle the string representations uniformly.
Syntax: There are no methods named str or repr directly callable on the instance (e.str() or e.repr()). Instead, str(e) and repr(e) are the correct ways to invoke the corresponding special methods.
"""



from partII import Employee

e = Employee("Harry")
print(str(e))
print(repr(e))
e()
# print(e.name)
# print(len(e))