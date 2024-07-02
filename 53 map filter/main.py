def sq(x):
    return x*x

l1 = [1,2,3,4]
l2 = []
# for i1 in l1:
#     l2.append(sq(i1))

l3 = list(map(sq,l1))

print(l3)

# filter
def filter_function(a):
    return a>4

l4 = list(filter(filter_function,l3))
print(l4)

demo = [3,4,5,6,7]
res = map(lambda x:x+1,demo)
print("the list is ", demo)
print("the new apply is ",list(res))

name = "aryan"
print("the name of the guy is", name)

# reduce
from functools import reduce

mul1 = [1,2,3,4,5]

def multiply1(a,b):
    return a*b

ans = reduce(multiply1,mul1)
print("the multiplication table is", ans)