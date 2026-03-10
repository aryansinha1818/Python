class Example:
    def __init__(self, a):
        self.a = a  # instance attribute
    
    def method1(self, b):
        self.b = b  # instance attribute
        print(f"self.a: {self.a}, self.b: {self.b}")
    
    def method2(self, c):
        print(f"self.a: {self.a}, c: {c}")

# Create an instance of Example
ex = Example(10)

# Call method1
ex.method1(20)
# Output: self.a: 10, self.b: 20

# Call method2
ex.method2(30)
# # Output: self.a: 10, c: 30

# # Access attributes
print(ex.a)  # Output: 10
print(ex.b)  # Output: 20
# print(ex.c)
