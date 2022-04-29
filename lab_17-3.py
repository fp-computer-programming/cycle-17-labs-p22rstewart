# RTS 4/10/22

# Creates class
class TV_remote():
    channel = 0
    volume_level = 0
    on = False

    # Defines function
    def to_string():
        return TV_remote
print(TV_remote.to_string())


# Creates class
class TV_remote:
    # Defines functions
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.On = False

    def to_string(self):
        return "Channel:", self.channel, "Volume:", self.volume, "On:", self.On


# Test
tv = TV_remote()
print(tv.to_string())
