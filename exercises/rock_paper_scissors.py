import random

user_score = 0
computer_score = 0
draw = 0

choices = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quite: ').lower()
    if user_input == 'q':
        break

    if user_input not in choices:
        continue
    

    random_number = random.randint(0,2)
    computer_pick = choices[random_number]
    print('Computer picks', computer_pick)

    if user_input == 'rock' and computer_pick == "scissors":
        print('You won!')
        user_score += 1

    elif user_input == 'scissor' and computer_pick == "paper":
        print('You won!')
        user_score += 1

    elif user_input == 'paper' and computer_pick == "rock":
        print('You won!')
        user_score += 1

    elif user_input == 'rock' and computer_pick == "rock" or user_input == 'scissors' and computer_pick == "scissors" or user_input == 'paper' and computer_pick == "paper":
        print('You drew!')
        draw += 1
    
    else:
        print('computer wins')
        computer_score += 1
    

print('You won', user_score, 'times')
print('Computer won', computer_score, 'times')
print('You drew', draw, 'times')

print('Goodbye sucker')

