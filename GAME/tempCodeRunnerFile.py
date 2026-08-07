import random
tries=0
num=random.randint(1,10)
print(num)


while True:
    guess=(int)(input("Enter a number: "))
    if num==guess:
        tries+=1
        print(f"YOU ARE RIGHT AT {tries}")
        break
    elif num<guess:
        tries+=1
        print("GO A LITTLE LOWER")
    elif num>guess:
        tries+=1
        print("GO A LITTLE UPPER")
    else:
        tries+=1
        print("SORRY!YOU ARE WRONG")
    

   
