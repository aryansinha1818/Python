marks = [3,4,5,"Harry",True, False]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print("this")
print(marks[-5])

a =1 
print(type(a))

if "Harry" in marks:
    print("yes")

if "rry" in "Harry":
    print(False)

print(marks)
print(marks[:])
# start,end,jump
print(marks[1:6:2])
# end not included
print(marks[2:5])
print(marks[:5])
print(marks[::-1])
print(marks[::2])
print(marks[-6])
print(marks[-4:-2:1])

marks.append("Aryan Sinha")
print("the new marks list", marks)

