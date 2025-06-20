class Figure:
    def get_area(self):
        raise NotImplementedError("Метод area() должен быть переопределён в дочернем классе")
    def __int__(self):
        return int(self.get_area())

    def __str__(self):
        return f"Фигура: {self.__class__.__name__}"


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}, area={self.get_area()}"
    
PI = 3.14159
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return PI * self.radius ** 2
    
    def __str__(self):
        return f"Circle: radius={self.radius}, area={self.get_area()}"
    

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"RightTriangle: base={self.base}, height={self.height}, area={self.get_area()}"


shapes = [
    Rectangle(4, 5),
    Circle(3),
    RightTriangle(3, 4)
]

for shape in shapes:
     # print(shape.get_area())
    print(str(shape))     
    print(int(shape))     
    print("------------------")
   