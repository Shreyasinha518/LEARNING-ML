import random
tries=0
num=random.randint(1,10)
print(num)


while True:
    guess=(int)(input("Enter a number: "))
    tries+=1
    if num==guess:
        
        print(f"YOU ARE RIGHT AT {tries}")
        break
    elif num<guess:
        
        print("GO A LITTLE LOWER")
    elif num>guess:
       
        print("GO A LITTLE UPPER")
    else:
        
        print("SORRY!YOU ARE WRONG")

   
