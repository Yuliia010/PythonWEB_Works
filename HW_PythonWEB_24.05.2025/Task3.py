import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

    def length(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other): 
        return self.radius == other.radius
    def __ne__(self, other): 
        return not (self.radius == other.radius)

  
    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()


    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self


c1 = Circle(10)
c2 = Circle(4)

print(c1 == c2)  
print(c1 < c2)         
print(c1 > c2)

c3 = c1 + 3
print(c3.radius)

c1 += 10
print(c1.radius)

c4 = c1 - 2
print(c4.radius) 

c1 -= 1
print(c1.radius)
