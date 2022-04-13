print('Welcome to the Adventure game!')

play = input('You wanna play? ').lower
if play != 'yes':
    quit(print('You quit'))

else:
    print("Let's play!")

playing = input("You live with your nagging wife who keeps arguing. You wanna move out or talk to her (move/talk)").lower()
if playing == 'move':
    playing = input('you move out and find yourself other women to be gold diggers. You wanna get back to your wife or find one suitable girlfriend (get-back/)').lower()

    playing = input('you ')

if playing == 'talk':
    playing = input('your wife changes and you decide to treat her. you take her to dinner or indoor cooking (dinner/cooking)')
    

else:
    print('you ')
