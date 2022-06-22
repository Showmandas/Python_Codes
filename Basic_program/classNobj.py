#class & oject

class Animal:
    Name="",
    Leg=""

    # def set_val(self,Name,Leg):
    #     self.Name=Name
    #     self.Leg=Leg

    def __init__(self,Name,Leg):
        self.Name=Name
        self.Leg=Leg

    def show(self):
        print(f"Name: {self.Name},Legs: {self.Leg}")



dog= Animal("tucky",4)
# print(isinstance(dog,Animal)) #true

# dog.Name='router'
# dog.Leg=4
# dog.set_val("hook",4)
dog.show()

# print(f"Name: {dog.Name},Legs: {dog.Leg}")