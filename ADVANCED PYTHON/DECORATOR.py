class Animal:
    @property #property decorator
    def show(self):
        print("Hello how are you?")
obj=Animal()
obj.show

def decorator(func):
    def wrapper(a,b):
        print("ADDITION IS ")
        func(a,b)
        print("THe addition is done")
    return wrapper
@decorator
def addition(a,b):
    print(f"The addition of the numbers is={a+b}")
addition (12,12)
