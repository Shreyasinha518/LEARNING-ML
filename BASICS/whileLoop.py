#a=1
#while a<=30:
 #   print(a)
  #  a+=1

n=(int)(input("Enter a number: "))
count=0
while(n>0):
    d=n%10
    count+=1
    n=n//10
print(count)

    
#Reverse
n=(int)(input("Enter a number: "))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print(rev)

#Palindrome
n=(int)(input("Enter a number: "))
a=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if(a==rev):
    print ("PALINDROME NUMBER: ",rev,"==",a)
else:
    print("NOT A PALINDROME NUMBER")