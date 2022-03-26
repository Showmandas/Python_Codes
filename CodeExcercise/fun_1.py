#Create a function that can accept two arguments name and age and print its value

def nameAge(name,age):
    print("my name is:",name)
    print("and my age is:",age)
nameAge("showman",23)

#list

def foods(food):
    for x in food:
        print(x)

fruits=['mango','apple','orange']

foods(fruits)

#arbitrary arguments

def names(*name):
    print(name[2])
names("shanu","showman","shantu")

def numbers(*num):
    for n in num:
       print(n)
numbers(20,30,40,50)

