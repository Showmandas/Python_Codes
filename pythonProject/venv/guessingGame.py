#guessing game
from random import  randint

count = 0

for x in range(1,6):
    guessnumber = int(input("Enter a guess number between 1 to 5: "))
    randnum = randint(1, 5)
    if(guessnumber==randnum):
       print("you have won")
       print("Your score is: ", count + 1)
    else:
       print("You have lost")
       print("the random number is: ",randnum)
