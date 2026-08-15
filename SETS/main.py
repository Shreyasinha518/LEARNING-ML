s={1,2,3,4,9,10,"hello",5,6,7,8}
print(s)
a=hash("hello")#shows no indexing
print(a)
b=hash((1,2,344))
print(b)
for i in s:
    print(i)
s.remove(10)
print(s)
s.pop()
print(s)
s.clear()
print(s)

x={1,2,9,8}
y={3,2,8,4}
z1=x.union(y)   #x|y
print(z1)
z2=x.intersection(y)  #x&y
print(z2)
z3=y-x
print(z3)
z4=x^y
print(z4)
