class Father:
    def height(self):
        print("Heieght is 6 feet")

class Mother:
    def color(self):
        print("mother color is brown")

class Child(Father,Mother):   #Child sub class is created from two super class father and mother, ths is example of multiple inheritance
    print("child is 6 feet and his color is brown")

c=Child()
print("inherited properties from parents")
c.height()
c.color()