#MEAN
l=[1,2,3,4,5,6,7,8,200,24,48,90,987]
sum=0
for i in l:
    sum=sum+i
print("The mean of list: ",sum/len(l))

#MAXIMUM
greatest=l[0]
index1=0
for i in range(len(l)):
    if l[i]>greatest:
        greatest=l[i]
        index1=i
print(f"The greatest element is : {greatest} at index :{index1}")

#SECOND LASRGEST
secondLargest=l[0]
index2=0
for i in range(len(l)):
    if(l[i]>secondLargest and l[i]!=greatest):
        secondLargest=l[i]
        index2=i
print(f"The second greatest element is : {secondLargest} at index :{index2}")

    
