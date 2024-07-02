class Person:
    # helps to create constructor
    # It is being called every time we create an object
    def __init__(self, n , o):
        print("Hey I am a person")
        #  n,o 2 arguments that we pass
        self.name = n
        self.occ = o
    # name="John"
    # work= "IT"

    # def info(self):
        print(f"The name is {self.name} and the occupation is {self.occ}")

a = Person("Aryan Sinha","Developer")
# b = Person()
c = Person("Divya","HR")
# c.info()
# print(a.name)
# a.info()

# a.info()