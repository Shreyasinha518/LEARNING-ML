d1={10:1000,20:2000,30:3000,40:7000}
d2={40:4000,50:5000,60:6000}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i] #adding value of key if it already exists
    else:   
        d1[i]=d2[i] #adding new key and value pair from d2 to d1
print(d1)