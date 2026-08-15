class Factory:   #private attribute and method
    __a="PUne"
    def show(self):
        print(f"Factory Location: {Factory.__a}")
obj=Factory()
obj.show()
    