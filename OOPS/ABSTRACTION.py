from abc import ABC, abstractmethod
class abstract(ABC):
    @abstractmethod #decorator
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class square (abstract):    #use of abstraction in python that we need to create area and perimeter also
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 4*self.side  
    def area(self):
        return self.side*self.side
class Circle (abstract):
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius*self.radius 
obj=Circle(7)
obj1=square(5)
print(f"Circle perimeter: {obj.perimeter()}, Circle area: {obj.area()}")
print(f"Square perimeter: {obj1.perimeter()}, Square area: {obj1.area()}")