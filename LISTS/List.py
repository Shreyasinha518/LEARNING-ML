a=[1,2,3,4,5,6,6.5,True,print()]
print(a[0])
print(a[6])
print(a[0:8])
print(a[-2])

n=[1,2,3,4,5,6,6.5]
for i in range(len(n)):
    print(n[i])
    
for i in n: 
    print(i)
n.append(100)
print(n)
n.insert(1,200)
print(n)
n.remove(200)
print(n)
print(n[4])
n[4]=20
print(n[4])
print(n)