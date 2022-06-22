#Method Overriding

class phone:
    def __init__(self):
        print("Phone classs")

class redmi_note(phone):
    #method override

    def __init__(self):
        super().__init__()  # use super class property
        print("redmi classs")


redmi=redmi_note()