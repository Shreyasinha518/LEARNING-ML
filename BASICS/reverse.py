a=input(("Enter a string:"))
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
print(b)
if b==a:
    print("PALINDROME")
else:
    print("NOT PALINDROME")


#concatination
a="Hello"
b=" World"
print(a+b)