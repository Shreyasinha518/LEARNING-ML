class Animal:       #method overriding
    def show(self):
        print("I am an animal.")
   # def show(self, name):          #python does not support method overloading, so the last defined method will override the previous one
       # print(f"I am an animal named {name}.")
class Human(Animal):
    def show(self):
        print("I am a human.")
obj=Human()




#Duck typing is a concept related to polymorphism in Python. It allows us to use objects of different classes interchangeably if they implement the same method or behavior, regardless of their actual class type.
class Dog:
    def sound(self):
        print("Woof!")          

class Cat:
    def sound(self):
        print("Meow!")

obj1 = Dog()
obj2 = Cat()    

obj1.sound()  # Output: Woof!
obj2.sound()  # Output: Meow!