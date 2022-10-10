#Types of inheritance

class A:
    def display1(self):
        print('A class')

class B(A):
    #display1()
    def display2(self):
        print('B class')

class C(B):
    #display1()
    #display2()
    def display3(self):
        print('C class')

obj1= C()
o
obj1.display2()
obj1.display3()
