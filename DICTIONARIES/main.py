d={1:"hello",2:"world",3:"python"} #key and value pair
print(d)
print(type(d))
print(d[3]) #accessing value using key
d[4]="programming" #adding new key and value pair
print(d)
d[1]="hi" #updating value of existing key
print(d)
d.update({5:"language"}) #adding new key and value pair using update method
print(d)
#dictionaries traversal
for i in d:
    #print(i)
    print(d[i]) #accessing value using key

#dictionaries methods
print(d.keys()) #returns all keys
print(d.values()) #returns all values
d2=d.get(3) #returns value of key 3
print(d2)
print(d.items()) #returns all key and value pair in tuple format
print(d.clear()) #removes all key and value pair from dictionary


#deep copy and shallow copy
a=[1,2,3,4,5,6,7,8,9,10]
b=a
b[0]=100
print(a) #shallow copy
c=a.copy() #deep copy
c[0]=200
print(c) #deep copy
print(a) #original list remains unchanged

