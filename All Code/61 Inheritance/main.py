# inherit the property from parent 
# class

"""
When a class is derived from a parent class, that class is called child class. the child class will have all the properties and methods of the parent class, in addition to this the child class can have its own properties as well this is called inheritance.
"""

# self - instead of that we can use any word, but the idea here is with the help of that we can access any variable present inside this class
class A:
    def displayA(self):
        print("Welcome to A")

# a class b ke andar chali gyi hai, a class ka saare behavior, methods b ke andar
class B(A):
    def displayB(self):
        print("Welcome to B")

print("New line")

class new(B):
    def display(self):
        print("New modifications made")

p1 = new()
p1.display()
p1.displayB()
p1.displayA()

class C(B):
    def displayC(self):
        print("Welcome to C")

obj = C()
obj.displayA();
obj.displayB();


# Multilevel inheritance
#  a b ke andar inherit, b c mein inherit hua
obj.displayC();
# inherit the property from parent 
# class

# self - instead of that we can use any word, but the idea here is with the help of that we can access any variable present inside this class
class E:
    def displayE(self):
        print("Welcome to E")
        # a class b ke andar chali gyi hai, a class ka saare behavior, methods b ke andar

class F:
    def displayF(self):
        print("Welcome to F")

class G(E,F):
    def displayG(self):
        print("Welcome to G")
obj = G()
obj.displayE();
obj.displayF();


# Multilevel inheritance
#  a b ke andar inherit, b c mein inherit hua
obj.displayG();