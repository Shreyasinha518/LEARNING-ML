a=(int)(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print("There is an error in your code",err)
else:print("There is no error in your code")
finally:
    print("The finally block is always executed")

print("division is done")
age=(int)(input("Enter your age: "))
try:
    if age>10 and age<18:
        raise ValueError("You are not eligible ")
    else:
        print("You are welcome to the club")
except ValueError as err:
    print("There is an error in your code",err)