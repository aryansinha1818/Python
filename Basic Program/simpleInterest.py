# si = p*r*t/100
def si(p,r,t):
    return (p*r*t)/100

p = "principal"
p = int(input())
r = "rate"
r = float(input())
t = "time"
t = int(input())

print("the simple interest is ", si(p,r,t))

