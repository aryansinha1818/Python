# Non-keyword (Positional) Arguments: Passed in a specific order and assigned to parameters based on their positions.
# Keyword Arguments: Passed using the parameter names, allowing you to specify values regardless of their order.
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet("Alice", 30)


# non-keyword
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet(name="Bob", age=25)

# combination of both
def greet(name, age, city):
    print(f"Hello, my name is {name}, I am {age} years old, and I live in {city}.")

greet("Carol", age=22, city="New York")
