class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    
a1 = MyClass(100)
print(a1.value)

# setter
class Game:
    def __init__(self, exercise):
        self._exercise = exercise
    @property
    def e1(self):
        return self._exercise
    @e1.setter 
    def e1(self, new_exercise):
        self._exercise = new_exercise 

chest = Game("bench press")
print(chest.e1)

chest.e1 = "pull over"
print(chest.e1)

# this has set the value as below
triceps = Game("skull curl")
print(triceps.e1)

# Now that set value is changed
triceps.e1 = "Overhead dumbbell"
print(triceps.e1)
