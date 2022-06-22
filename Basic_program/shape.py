#Triangle and rectangle


class Shape:
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2

    def Area(self):
        print("This is area")


class Triangle(Shape):     #inheritance
    #method overrite
    def area(self):
        res=0.5 * self.d1 * self.d2
        print("Triangle area : ",res)

class Rectangle(Shape):
    def area(self):
        res= self.d1 * self.d2
        print("Rectangle area : ",res)


t=Triangle(10,20)
t.area()

r=Rectangle(10,20)
r.area()

