# by accessing the tuple
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

def age(*age):
    print("the ages are",age[0],age[1])

age("two","three")