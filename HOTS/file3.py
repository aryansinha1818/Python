def fun1():
    print("hello my name is Aryan!")

# if we are running from the main file then only run this function 
if __name__ == "__main__":
    fun1()

# When we import a module in Python, all top-level code inside that file gets executed.
# To prevent unintended execution, we use if __name__ == "__main__".
# This ensures that certain code runs only when the file is executed directly, not when it is imported.