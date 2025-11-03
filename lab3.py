class Shape:
    def area(self):
        pass  

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(3, 3), Circle(3)]
for i in range(len(shapes)):
    print(shapes[i].area())