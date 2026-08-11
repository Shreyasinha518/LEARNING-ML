a="ab1234@#$asdrf"
char=0
dig=0
spchar=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
print(f"The number of digits = {dig} \n The number of aplhabets = ={char}\n The number of special characters = {spchar}")
#print(dir(a)) --STRING DIRECTORIES