import random

emojis={'rock':'🪨','paper':'📃','scissors':'✂️'}
choices=('rock','paper','scissors')
while True:

    choice=input("ROCK,PAPER or SCISSORS?(Rock/Paper/Scissors):").lower()
    if choice not in choices:
        print("Invalid Choice!")
        continue

    comp=random.choice(choices)

    print(f'You have chosen {emojis[choice]}')
    print(f'Computer Chose {emojis[comp]}')

    if choice ==comp:
        print("TIE!")
    elif (choice=='rock' and comp=='scissors') or \
        (choice=='scissors' and choice=='paper') or \
        (choice=='paper' and choice=='rock'):
        print("YOU WIN!🥳")
    else:
        print("BETTER LUCK NEXT TIME..")    
    permission=input("Do you wanna continue?(Yes/No):")   
    if permission=='no':
        break
    elif permission=='yes':
        continue
    else:
        break



 

