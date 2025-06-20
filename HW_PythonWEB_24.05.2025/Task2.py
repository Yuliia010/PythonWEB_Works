#import pickle

class Shape:
    def show(self):
        raise NotImplementedError("Not Implemented Error")

    def getInfo(self):
        return "no info"

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.getInfo())
        print("The file has been written.")

    @staticmethod
    def load(filename):
        result = ""
        with open(filename, 'r') as file:
            for line in file:
                result += line
        return result

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def getInfo(self):
        return f"Square: Top-left corner = ({self.x}, {self.y}), Side = {self.side}"
    
    def show(self):
        print(self.getInfo())

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getInfo(self):
        return f"Rectangle: Top-left corner = ({self.x}, {self.y}), Width = {self.width}, Height = {self.height}"

    def show(self):
        print(self.getInfo())

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def getInfo(self):
        return f"Circle: Center = ({self.center_x}, {self.center_y}), Radius = {self.radius}"

    def show(self):
        print(self.getInfo())

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getInfo(self):
        return f"Ellipse: Bounding box top-left = ({self.x}, {self.y}), Width = {self.width}, Height = {self.height}"

    def show(self):
        print(self.getInfo())




sq = Circle(5, 5, 20)
sq.show()
sq.save("test.txt")
ts = Shape.load("test.txt")
print(ts)