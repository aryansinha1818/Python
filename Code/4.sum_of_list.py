# list1 = [1,2,3,4]
# sum = 0
# for i in list1:
#     sum=sum+i 

# print(sum)

n = int(input("Enter the size of the list "))
list1 = []

for i in range(0,n):
    x = int(input())
    list1.append(x)

sum = 0
for i in list1:
    sum=sum+i 

print(sum)