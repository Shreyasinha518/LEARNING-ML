def hello():
    print("THIS IS HELLO FUNCTION")
hello()   #Runs only when called

def sum(a,b):
    print ("SUM IS : ",a+b)
a=(int)(input("Enter first number:"))
b=(int)(input("Enter second number:"))
sum(a,b)
sum(100,100)

def hello(name,age):
    print(f"Your name is {name} and your age is {age}")
hello(age=20,name="Shreya")

def sum(a,b=100):
    print ("SUM IS : ",a+b)
sum(100)
sum(2,4)
