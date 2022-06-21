
class dog:
    """Representing a dog"""
    def __init__(self,_name,_color,_age):
        self.name=_name
        self.color=_color
        self.age=_age

        def get_name(self):
            return self.name
        def get_color(self):
            return self.color
        def get_age(self):
            return self.age

mydog=dog('pusshy','brown',2)
print(mydog)

