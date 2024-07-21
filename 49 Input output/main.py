"""
By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.
"""
# would give error when not exists
f = open('f1.txt', 'r')

print(f) 

wrt = open("f1.txt",'w')
wrt.write("Hello my name is Aryan Sinha")
wrt = open("f1.txt",'r')
st = wrt.read()
print(st)

with open('f1.txt','w') as s:
    for i in range(10):
        s.write(str(i))