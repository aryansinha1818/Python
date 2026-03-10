class Aryan:
    def __init__(self):
        self.__word = "Aryan "
        # below public
        self.word1 = "Sinha" 
        # below protected
        self._word2 = "He is very successful"
        print("Hey I am super cool")
    
a = Aryan();
print(a._Aryan__word);
print(a.word1)
print(a._word2)