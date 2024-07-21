"""def function_name_print(a,b,c,d):
    print (a,b,c,d)"""

def function_name_print(*args):
    print(args[0])

function_name_print("Aryan","Sinha","Koshik","Nitin")

l1 = ["D","E","F","G"]
letters = "the following are"

def f2( *argscat):
    # print(args)
    for item in argscat:
        print(item)

f2(letters,*l1)
f2(l1)

"""Kwargs"""
def func(**kwargs):
    # print(**kwargs)
    print("print the message")
    # .items(): This method returns a view object containing the key-value pairs of the dictionary as tuples
    for item,key in kwargs.items():
        print(f"the key is {item} and the value is {key}")

d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "month": "July"
}
func(**d1)