class Factory:
    a = 12  # attribute

    def hello(self):  # method
        print("Hello from Factory class")

    print("I am getting initialized when the class is loaded")


Factory().hello()
print(Factory().a)

obj = Factory()  # object of the class
obj.a
obj.hello()


# constructor
class Factory:
    def __init__(self, material, zips, pockets):
        print(self)  # location of the object in memory
        self.material = material
        self.zips = zips
        self.pockets = pockets

    # Added this method (required after redefining the class)
    def hello(self):
        print("Hello from Factory class")

    def show(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")


reebok = Factory("leather", 3, 2)
campus = Factory("nylon", 3, 3)

reebok.show()
campus.show()

print(campus.zips)
print(reebok.pockets)
print(campus.pockets)


# ATTRIBUTES AND METHODS
class Animal:
    def __init__(self, age):
        self.age = age  # instance attribute

    def show(self):  # instance method
        print(f"How are you, your age is: {self.age}")

    @classmethod
    def hi(cls):  # class method
        print("Hello from class method")

    @staticmethod
    def static():  # static method
        print("Hello from static method")


obj = Animal(12)

obj.show()

obj.hi()         # object can call class method
Animal.hi()      # class can call class method

obj.static()     # object can call static method
Animal.static()  # class can call static method


# inheritance
class Factory1(Factory):
    pass  # child class


obj = Factory("Leather", 3, 2)
obj1 = Factory1("Nylon", 2, 4)

obj.hello()
obj1.hello()

obj.show()
obj1.show()
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Animal name is: {self.name}")


class Human(Animal):

    def __init__(self, name, age):
        super().__init__(name)   # Calling parent class constructor
        self.age = age

    def show(self):
        print(f"Human name is: {self.name} and age is: {self.age}")


# Objects
animal1 = Animal("Dog")
human1 = Human("John", 25)

animal1.show()
human1.show()

#MULTIPLE INHERITANCE
class Animal:
    def __init__(self, name):
        pass
class human:
    def __init__(self, name,age):
        pass
class Robots(Animal,human): #first class will be given priority in case of same attribute name,first class is inherited class
        pass
obj=Robots("Robo")
