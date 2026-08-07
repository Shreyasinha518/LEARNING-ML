a=[1,2,3,4,5,6]     #map applies same functionto every object in the list
#result=map(lambda x:x*2,a)
def double(x):
    return x *2
result=map(double,a)
print(list(result))

#def even(x):
    #if x%2==0:
     #   return True
    #else:
    #    return False
a=[1,2,3,4,6,8,10,18,20]   #Filter -filer outs the element not following the function
result=filter(lambda x:True if x%2==0 else False,a)
print(list(result))
