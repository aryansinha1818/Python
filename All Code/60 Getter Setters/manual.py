class TV:
    def __init__(self, channel):
        # below is the public
        self.channel = channel
    
ch1 = TV(9)
print(ch1.channel)

ch1.channel = 10
print("the changes channel is", ch1.channel)