class Shape():
    """docstring for Shape."""
    def __init__(self):
        super(Shape, self).__init__()
    def what_am_I(self):
        print('I am a %s' % (self.__class__.__name__))

class Rectangle(Shape):
    """docstring for Rectangle."""
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def calculate_area():
        return self.length*self.width

class Square(Shape):
    """docstring for Square."""
    def __init__(self, s):
        self.sides = s
    def calculate_area(self):
        return self.sides*self.sides
    def changes_size(self, new_size):
        if new_size > 0:
            self.sides = self.sides + new_size
        elif new_size < 0:
            if abs(new_size) < self.sides:
                self.sides = self.sides + new_size
            else:
                print('Cannot be negative')

sq_1 = Square(6)
rec_1 = Rectangle(10, 4)
print(sq_1.calculate_area())
sq_1.changes_size(-1)
rec_1.what_am_I()
