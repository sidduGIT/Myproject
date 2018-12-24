class Father:
    def __init__(self,property=0):
        self.property=property

    def display_property(self):
        print("Fathers property ", self.property)

class Son(Father):
    def __init__(self,property1=0,property=0):
        super().__init__(property) #send property value to super class father
        self.property1 = property1

    def display_property(self):
        print("Sons property    {}  \nFathers property   {}".format(self.property1,self.property))
s=Son(2000000,8000000)
s.display_property() #now both property wll be dsplayed as we defined super constructor for fathers constructor


class Square:
    def __init__(self,x=0):
        self.x=x

    def area(self):
        print("Area of square is",self.x*self.x)

class Rectangle(Square):
    def __init__(self,x=0,y=0):
        super().__init__(x)  #super class
        self.y=y

    def area(self):
        super().area()  #super method
        print("Area of rectangle is", self.x * self.y)


a,b=[float(x) for x in input("enter length and bredth").split()]
r=Rectangle(a,b)
r.area()

