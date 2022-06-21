#Create an inner function to calculate the addition

def outerfun(a,b):

    def innerfun(a,b):
        # add=a+b
        return a+b
    return a+b+5

print(outerfun(10,20))
