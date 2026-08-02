#MULTILEVEL INHERITANCE
class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips
    def show(self):
            print(f"Material: {self.material}, Zips: {self.zips}")
class BhopalFactory(Factory):
    def __init__(self, material, zips, colors):
        super().__init__(material, zips)  # calling the parent class constructor
        self.colors = colors

    def show(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Colors: {self.colors}")
class PuneFactory(BhopalFactory):
    def __init__(self, material, zips,colors, pockets):
        super().__init__(material, zips, colors)  # calling the parent class constructor
        self.pockets = pockets

    def show(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Colors: {self.colors}, Pockets: {self.pockets}")

obj=PuneFactory("Leather", 3, "Black", 2)
obj.show()