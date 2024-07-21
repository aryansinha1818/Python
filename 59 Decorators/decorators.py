def outer_func(inner_func):
    def wrapper():
        print("Start")
        inner_func()
        print("End")

    return wrapper

"""Instead of the below we do this"""
# The @outer_func syntax above inner_func is a decorator. This is syntactic sugar for inner_func = outer_func(inner_func). 
# It automatically passes inner_func to outer_func and assigns the returned wrapper function back to inner_func.
@outer_func
def inner_func():
    print("Inner Function")

"""
Instead of below we do this
"""
# x = outer_func(inner_func)
# x()

# Define inner_func: The inner_func is defined to print "Inner Function".

# Execute inner_func: When inner_func() is called, it actually calls the wrapper function created by outer_func.
inner_func()