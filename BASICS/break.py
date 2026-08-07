for i in range(1,21):
    if i==15:
        break     #yaha pe 15 ke baad kuch print nhi hua
    else:
        print(i);
for i in range(1,21):
    if i==15:
        continue   #yaha pe sirf 15 skip hua
    else:
        print(i);

n=(int)(input("Enter a number: "))
for i in range(n):
    print("hellow world")
for i in range(1,n+1,1):
    print(i)
for i in range (n,0,-1):
    print(i)