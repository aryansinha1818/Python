def outer_func(inner_func):
    def wrapper():
        print("Start")
        inner_func()
        print("End")

    return wrapper

def inner_func():
    print("Inner Function")

# it only returns the outer function without calling it
outer_func(inner_func) 

# everything in py is an object, when called prints the function object, hexadecimal is the memory address where the function wrapper inside the outer function is stored
print(outer_func(inner_func))

# instance is created and a memory is assigned
op = outer_func(inner_func)
print(f"the op is {op}")
# when we call the wrapper function object, it executes and prints accordingly
op()