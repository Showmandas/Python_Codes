from typing_extensions import Self


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show_details(self):
        print("Name of person: ",self.name)
        print("Age of person: ",self.age)



class student(person):
    def __init__(self, name, age,gender,id):
        super().__init__(name, age)
        self.gender=gender
        self.id=id
    
    def show_std(self):
        print("Gender of student: ",self.gender)
        print("Id of student: ",self.id)
    

obj=student('sanu',24,'male',2)

print(obj.show_std())
    


        