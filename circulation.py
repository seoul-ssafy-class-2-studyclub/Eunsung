class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point({self.x},{self.y})'

class Circle:

    def __init__(self, center, r):
        self.center = center
        self.r = r
    
    def get_area(self):
        return self.r**2*3.14
    
    def get_perimeter(self):
        return self.r*2*3.14

    def get_center(self):
        return f'{self.center}'
    
    def __str__(self):
        return f'Circle:{self.center}, r:{self.r}'
        