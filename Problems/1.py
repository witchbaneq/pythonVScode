class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_area(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)
    
Rect  = Rectangle(34,34,232,324)
print(Rect.get_area())