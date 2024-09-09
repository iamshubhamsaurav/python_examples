#Inheritance example

class Human:    
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name is ", self.name)


class Man(Human):
    def __init__(self, name, country):
        super().__init__(name)
        self.country = country

    def printCountry(self):
        print("Country: " + self.country)


human1 = Human("XYZ")
human1.printName()

print("Man Object")
man1 = Man("ABC", "INDIA")
man1.printName()
man1.printCountry()