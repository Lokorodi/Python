import random

top_of_range = input('Type a number: ')


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print('Type a number greater or equal to 0')

else:
    print('Type a number next time')
    quit(print('Goodbye sucker'))

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
       continue

    if user_guess == random_number:
        print('you got it!')
        break
    elif user_guess > random_number:
        print('You are above thhe number')
    else:
        print('you are below the number')
        continue

print('You got it in', guesses, 'guess')



