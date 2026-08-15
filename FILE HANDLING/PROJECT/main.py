from pathlib import Path
import os
def readFileAndFolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}. {items}")
def readfile():
    try:
        readFileAndFolder()
        name=input("Please enter the name of the file you want to read: ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data=fs.read()
                print(data)
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def updatefile():
    readFileAndFolder()
    name=input("Please enter the name of the file you want to update: ")
    p=Path(name)
    if p.exists() and p.is_file():
        print("press 1 for changing the data in the file")
        print("press 2 for overwriting the data in the file")
        print("press 3 for appending the data in the file")

        res=int(input("Please tell your response: "))
        if res==1:
            name2=input("Please enter the name of the file you want to change the data with: ")
            p2=Path(name2)
            p.rename(p2)
            print("File name changed successfully")
        if res==2:
            with open(p, "w") as fs:
                data=input("Please enter the data you want to write in the file,this will overwrite the data: ")
                fs.write(data)
            print("File overwritten successfully")
        if res==3:
            with open(p, "a") as fs:
                data=input("Please enter the data you want to append to the file: ")
                fs.write(data)
            print("Data appended successfully")

def deletefile():
    readFileAndFolder()
    name=input("Please enter the name of the file you want to delete: ")
    p=Path(name)
    if p.exists() and p.is_file():
        os.remove(p)   #p.unlink() can also be used to delete the file
        print("File deleted successfully")
    else:
        print("File does not exist")

def createfile():
    try:
        readFileAndFolder()
        name=input("Please enter the name of the file you want to create: ")
        p=Path(name)
        if not p.exists() and not p.is_file():
            with open(p, "w") as fs:
                data=input("Please enter the data you want to write in the file: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as e:
        print(f"An error occurred: {e}")
   
    

print("PRESS 1 FOR CREATING A FILE")
print("PRESS 2 FOR READING A FILE")
print("PRESS 3 FOR UPDATING A FILE")
print("PRESS 4 FOR DELETING A FILE")
check=(int(input("Please tell your response: ")))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    deletefile()