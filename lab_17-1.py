# RTS 4/10/22

# Importing math moduel
import math


class Circle:
    # Defining function
    def __init__(self):
        self.radius = 3

    def get_diameter(self):
        return self.radius * 2

    def get_area(self):
        return math.pi * self.radius ** 2


# Test
my_circle = Circle()
print(my_circle.get_area())
