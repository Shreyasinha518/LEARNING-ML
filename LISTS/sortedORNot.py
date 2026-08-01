lst= list(map(int, input("Enter numbers: ").split()))
print(lst)
l = lst.copy() 
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print (l)
if l == lst:
    print("LIST IS ALREADY SORTED")
else:
    print("LIST IS NOT SORTED")