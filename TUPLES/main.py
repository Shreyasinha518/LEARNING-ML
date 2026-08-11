a=(1,2,4,6,8,9,5,3,6,6,6,print(),9.6,"hello")
print(type(a))
print(a[0])
for i in a:   #tuple access
    print(i)
for i in range(len(a)):  #acess by index
    print(a[i])
index=a.index(6)
print(index)
count=a.count(6)
print(count)

a,b,c,d=(1,2,3,4)    #unpacking
print(type(a))
print(a)
print (d)