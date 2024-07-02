# fact - 4! = 4*3*2*1

def fact(n):
    # shorthand
    return 1 if(n==1 or n==0) else n*fact(n-1)

n1 = int(input())
print("The fact of ",n1," is ",fact(n1))

