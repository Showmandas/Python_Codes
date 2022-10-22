
Max_lines=3
Max_bet=100
Min_bet=1


def deposit():
    while True:
        amount=input('What would you like to deposit? $')
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print('Please enter a number')
    return amount

def get_num_of_lines():
    while True:
        lines=input('Enter the number of lines to bet on (1-' + str(Max_lines) + ')? ')
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= Max_lines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print('Please enter a number')
    return lines

def get_bet():
    while True:
        amount=input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount=int(amount)
            if Min_bet <= amount <= Max_bet:
                break
            else:
                print(f"amount must be between ${Min_bet} to ${Max_bet}.")
        else:
            print('Please enter a number')
    return amount




def main():
    balance=deposit()
    lines=get_num_of_lines()
    bet=get_bet()
    total_bet=bet * lines
    print(f"you are betting ${bet} on ${lines} lines. Total bet is equal to : ${total_bet}")
    print(balance,lines)

main()