'''Object-Oriented, Ch. 12'''
import math

class Circle(object):
    """docstring for Circle."""
    def __init__(self, radius):
        super(Circle, self).__init__()
        if radius <= 0:
            raise ValueError('Value must be greater than 0')
        self.radius = radius

    def area(self):
        return self.radius**2 * math.pi

cir_1 = Circle(6)

print(cir_1.area())
