def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args,**kwargs)
        print("Ended")
    
    return wrapper

@f1
def lol(a, name, age) :
    print(a,name, age)

# lol("Hi")
lol("Hi, my name is","Aryan", "and my age is ", age = 25)
