class ParentClass:
    def parent_method(self):
        print("This is the parent method")
    
    def child_method(self):
        print("This is parent version")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method")
        super().parent_method()

q2 = ParentClass()
q2.child_method()
q2.parent_method()
q1 = ChildClass()
q1.child_method()