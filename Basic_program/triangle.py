#Determine Triangle Area

class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calculation_area(self):
        print(f"Area: {0.5 * self.base* self.height}")


triangle_1=Triangle(10,20)
triangle_1.calculation_area()

triangle_2=Triangle(20,30)
triangle_2.calculation_area()