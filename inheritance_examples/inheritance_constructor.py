'''class Father:
    def __init__(self):
        self.property=8000000

    def display_property(self):
        print("Fathers property ",self.property)
class Son(Father): #created son subclass from father super class
    pass
s=Son()
s.display_property() #displaying fathers property'''

class Father:
    def __init__(self):
        self.property=8000000

    def display_property(self):
        print("Fathers property ", self.property)

class Son(Father):
    def __init__(self):
        self.property = 2000000

    def display_property(self):
        print("Sons property ", self.property)
s=Son()
s.display_property() #sons property will be displayed as son is also having a constructor and super class constructor is overridden