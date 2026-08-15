p = open(r"C:\Users\Shrey\OneDrive\Desktop\CIVIQUE\frontend\node_modules\baseline-browser-mapping\LICENSE.txt")
print("File opened successfully")
print(p.read())
p.close()
with open("FILE HANDLING/superman.txt", "a") as a:
    a.write(" and I am writing this line in it")

print("File written successfully")