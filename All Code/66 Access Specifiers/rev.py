# Public
"""# Public members are accessible from anywhere.
# By default, all members (attributes and methods) of a class are public.
# No special syntax is required.

class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"

    def public_method(self):
        return "This is public method"
    
obj = MyClass()
print(obj.public_attribute)
# Method called with bracket
print(obj.public_method())"""

# class MyClass:
#     def __init__(self):
#         self._protected_attribute = "I am protected"

#     def _protected_method(self):
#         return "This is a protected method"

# class SubClass(MyClass):
#     def access_protected(self):
#         return self._protected_attribute

# obj = SubClass()
# print(obj.access_protected())  # Accessible within subclass
# print(obj._protected_method()) # Accessible but discouraged outside the class
# print(obj._protected_attribute)

# Private
# Private members are intended to be accessible only within the class.
# A double underscore (__) prefix is used to indicate that a member is private.
# Python performs name mangling to make it harder to access private members from outside the class.

class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "This is a private method"

    def access_private(self):
        return self.__private_method()

obj = MyClass()
# print(obj.__private_attribute)  # Raises AttributeError
# print(obj.__private_method())   # Raises AttributeError
print(obj.access_private())       # Accessible through class method

# Name Mangling
"""The name mangling for private members changes their name to include the class name.
This makes it more challenging to accidentally access private members."""
print(obj._MyClass__private_method)
print(obj._MyClass__access_private())

# Name mangling is a mechanism in Python used to make private class attributes more difficult to access from outside the class. It involves altering the names of private variables to include the class name as a prefix, making it harder to accidentally access or modify these variables from outside the class scope.

# How Name Mangling Works
When you define a class attribute or method with a double underscore prefix (e.g., __private), Python internally changes its name to include the class name. This process is known as name mangling.