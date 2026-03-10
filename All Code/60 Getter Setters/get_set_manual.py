class TV:
    def __init__(self, channel):
        self._channel = channel
    
    def get_channel(self):
        return self._channel
    
    def set_channel(self, channel):
        if 0 <= channel <= 100:
            self._channel = channel
        else:
            print("Invalid Channel Number")
        
ch1 = TV(10)
print(ch1.get_channel())
ch1.set_channel(120)
print(ch1.get_channel())