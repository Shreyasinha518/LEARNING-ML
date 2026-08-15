a=[1,24,6,7,4,6,4,3,2,1,2,3,4,5,6,7,8,9,10]
count={}
for i in a:
    if i in count.keys():
        count[i]+=1 #incrementing the value of key if it already exists
    else:
        count[i]=1 #adding new key and value pair if it doesn't exist

print(count)