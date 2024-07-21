# single expressions
# def double(x):
#     return x*2

double = lambda x:x*2
cube = lambda x:x*3

print(double(3.2))
print(cube(5))


aryan = lambda x:x+8
print(aryan(1))

a = lambda num: num*2
print(a(10))

b = lambda str: str+"Hello World!"
print(b("I am python and I say,"))

c = lambda num1, num2: num1*num2
print(c(10,10))

def app(fx, value):
    return 6 + fx(value)

print(app(lambda x: x+10, 10))