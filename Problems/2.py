import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        return math.pi * self.r * self.r
    
    @staticmethod
    def is_valid_radius(r):
        return r > 0
            
    

circle = Circle(28,12,10)
print(circle.is_valid_radius(circle.r))
print(circle.get_area())