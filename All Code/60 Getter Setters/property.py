class TV:
    def __init__(self, channel):
        self._channel = channel
    
    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, channel):
        if 0 <= channel <= 100:
            self._channel = channel 
        else:
            print("Invalid channel number")
        
ch1 = TV(10)
print(ch1.channel)

ch1.channel = 99
print(ch1.channel)

ch1.channel = 150
print(ch1.channel)
