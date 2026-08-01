t=(int)(input("Enter the temprature: "))
if t<0:
    print("FREEZING POINT")
elif t>0 and t<20:
    print("cold")
elif t>=20 and t<30:
    print("pleasent")
elif t>=30 and t<40:
    print("hot")
else:
    print("Temprature is very hot")
