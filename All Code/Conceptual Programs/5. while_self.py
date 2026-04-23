num = int(input("Enter the number"))
# while num!=0:
#     print("valid number")
#     break
# else:
#     print("wrong number")
count = 0
num = 0
while num < 10:
    num = int(input("Enter the number"))
    count += 1
    if(count >= 7):
        print("Max tries reached!!")
        break
    if num < 10:
        print("valid number")