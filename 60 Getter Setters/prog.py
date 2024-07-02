class Student:
    __name = "Aryan"
    # private variable
    # private function
    def __pFunc(self):
        print("Hello I am private function")
    def __init__(self):
        print(self.__name)
        self.__pFunc()
    
    # not valid below
    # def __init__(self):
    #     print(self.__pFunc)

obj = Student();
 
# print(obj.name)
# print(obj.__pFunc)