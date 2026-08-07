n=(int)(input("Enter then number"))
sum=0
fact=1
for i in range(1,n+1):
    sum=sum+i

print("Sum of number is: ",sum)
for i in range(n,0,-1):
    fact=fact*i

print("Factorial of number is: ",fact)
for i in range(1,n+1):
 if n%i==0:
     print(i)
     


even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)

print("Factorial of number is: ",fact)
sum=0
for i in range(1,n):
 if n%i==0:
     sum=sum+i
if sum==n:
   print("perfect number")

else:
   print("not a perfect number")
#prime number
a=(int)(input("Enter a number"))
count=0
for i in range(1,a+1):
   if a%1==0:
    count=count+1
if count==2:
   print(" prime number")
else:
   print(" composite number")


