x = 10

def my_func():
    global x 
    x = 5
    y = 5

my_func()
print(x)
# print(y)