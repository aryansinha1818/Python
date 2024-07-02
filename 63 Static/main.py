class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
       self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b

a = Math(5)
# More preferable 
print(Math.add(1,5))
print(a.add(1,7))
