# def f1():
#     print("called f1")

# print(f1)
# print(f1())

def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper

def f():
    print("Hello")

# f1(f())
f1(f)
f1(f)()