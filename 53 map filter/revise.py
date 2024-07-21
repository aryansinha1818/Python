# Traditional Approach


def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,3,4,5]
nl = []
# for item in l:
#     nl.append(cube(item))

# print(nl)
newl = list(map(cube,l))
print(newl)


num = [1,2,3,4,5]
doubled = map(lambda x: x*2, num)
print(list(doubled))

cut = filter(lambda x: x>2, num)
print(list(cut))

from functools import reduce
red = reduce(lambda x,y: x+y,num)
print(red)
