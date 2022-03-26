class employee:
    __name= None
    __age= 0

    def set_name(self, name):
        self.__name=name
    def set_age(self, age):
        self.__age=age

    def get_name(self):
            return self.__name
    def get_age(self):
        return self.__age


emp=employee()
emp.set_name("shanu")
emp.set_age(24)
print(emp.get_name())
print(emp.get_age())