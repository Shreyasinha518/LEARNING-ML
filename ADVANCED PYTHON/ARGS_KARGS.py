def addition(*args):   #now elements become tuple
    sum=0
    for i in args:
        sum+=i
    print(sum)
addition(1,2,3,4,5,6,7,8,9,10)


def numbers (**kwargs):    #now elements are dictionaries
    print(kwargs)
numbers(a=10,b=20,c=30)

def information (**kwargs):
    print("Print your information is \n\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name="Shreya",age=20,designation="student")
    