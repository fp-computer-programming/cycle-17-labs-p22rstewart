# RTS 4/10/22

import math


# Creates class
class Circle:
    # Defining functions
    def __init__(self):
        self.radius = 3

    def get_diameter(self):
        return self.radius * 2

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


# Test
my_circle = Circle()
print(my_circle.get_perimeter())
