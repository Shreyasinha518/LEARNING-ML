class Factory:
    a=12 #attribute
    def hello(self):  #method
        print("Hello from Factory class")
    print("I am getting intialized when the class is loaded")
Factory().hello()
print(Factory().a)