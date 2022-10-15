from traceback import print_tb


class Vehicle:
    def __init__(self,model,cost):
        self.model=model
        self.cost=cost
    
    def show_details(self):
        print("Model of the vehicle:",self.model)
        print("Cost of the vehicle:",self.cost)
        print('This is vehicle class')
    


#Creating Child class
class Car(Vehicle):
    def show_car(self):
        print('This is sub class car')



c1=Car('Noah',2000000)   # Instantiating  the object  for child class
print(c1.show_details()) 
print(c1.show_car())
