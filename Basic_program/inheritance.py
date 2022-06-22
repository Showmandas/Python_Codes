#inheritance

class cat:      #super class
    def body(self):
        print("two eyes!!four legs")


class dog(cat):
    def head(self):
        print("two eyes!!two ears")

class animal(dog,cat):  #subclass
    def CatDog(self):
        print("Cat and Dog both are animal!")

# Dog=dog()
# Dog.head()
# Dog.body()
Animal=animal()
# Animal.head()
# Animal.body()
print(issubclass(animal,cat))
