class Airplane:
    def __init__(self, model, passengers, max_passengers):
        self.model = model                      
        self.passengers = passengers           
        self.max_passengers = max_passengers    

    def __str__(self):
        return f"Airplane(model={self.model}, passengers={self.passengers}, max={self.max_passengers})"

  
    def __eq__(self, other):
        return self.model == other.model

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __add__(self, value):
        return Airplane(self.model, self.passengers + value, self.max_passengers)

    def __sub__(self, value):
        return Airplane(self.model, self.passengers - value, self.max_passengers)

    def __iadd__(self, value):
        self.passengers += value
        return self

    def __isub__(self, value):
        self.passengers -= value
        return self


a1 = Airplane("Test type 1", 100, 180)
a2 = Airplane("Test type 2", 120, 160)
a3 = Airplane("Test type 1", 90, 180)

print(a1 == a3)        
print(a1 == a2)  

print(a1 > a2)    
print(a1 < a2)  

a4 = a1 + 20           
print(a4.passengers)   

a1 += 10               
print(a1.passengers)   

a5 = a1 - 5
print(a5.passengers)   

a1 -= 15
print(a1.passengers)   
