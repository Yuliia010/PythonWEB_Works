class Flat:
    def __init__(self, area, price):
        self.area = area    
        self.price = price  

    def __str__(self):
        return f"Flat(area={self.area}, price={self.price})"

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return not self == other


    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price



f1 = Flat(60, 80000)
f2 = Flat(60, 90000)
f3 = Flat(45, 70000)

print(f1 == f2)  
print(f1 != f3)  

print(f2 > f1)   
print(f3 < f2)   
print(f3 >= f1)  
