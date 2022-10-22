import random

user=0
computer=0
options=['rock','paper','scissors']

while True:
    user_inp=input('Type Rock/Paper/Scissors or q to quit the program: ').lower()
    if user_inp == 'q':
        break

    if user_inp not in options:
        continue
    
    rand_num=random.randint(0,2)
    computer_pick=options[rand_num]
    print('Computer Picked',computer_pick+'.')

    if user_inp=='rock' and computer_pick == 'scissors':
        print('You win!')
        user+=1
    
    elif user_inp=='paper' and computer_pick == 'rock':
        print('You win!')
        user+=1
    
    elif user_inp=='scissors' and computer_pick == 'paper':
        print('You win!')
        user+=1
    
    else:
        print('You lost!')
        computer+=1

print('You won',user,'times')
print('Machine won',computer,'times')
print('Game Finished!')