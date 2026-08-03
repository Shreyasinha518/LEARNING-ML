class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return(f"Hello how are you and your name is {self.name}")
    def __add__(self, other):
        return f"your sum of ages {self.age + other.age}"
obj1=Animal("Lion",12)
obj2=Animal("Dolphin",14)

print (obj1 + obj2)