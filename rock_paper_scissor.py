import random

user_win = 0
computer_win = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("please enter Rock/Paper/scissors Or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0 , paper: 1, scissors: 2
    computer_pick = options[random_number]
    
    print('computer picked', computer_pick + '.')
    
    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_win += 1
    
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_win += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!")
        user_win += 1
    
    elif computer_pick == 'rock' and user_input == 'scissors':
        print("Computer won!")
        computer_win += 1
    
    elif computer_pick == 'paper' and user_input == 'rock':
        print("Computer won!")
        computer_win += 1

    elif computer_pick == 'scissors' and user_input == 'paper':
        print("Computer won!")
        computer_win += 1
    
    else:
        print("Draw!")
        continue
        
        
print(f'You won {user_win} times.')
print(f'You won {computer_win} times.')        
print('Goodbye!, Thank You for playing')