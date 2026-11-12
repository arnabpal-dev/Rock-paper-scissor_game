import random

choices=('r','p','s')
emojies={'r':'🪨','p':'📃','s':'✂️'}

while True:
    com_choice=random.choice(choices)
    user_choice=input("rock,paper,or scissors? (r/p/s)")

    if user_choice not in choices:
        print("not in option")
        continue  

    print(f'you chose{emojies[user_choice]}')
    print(f'computer chose{emojies[com_choice]}')

    if user_choice==com_choice:
        print("tie!")
    elif\
        (user_choice=='r'and com_choice=='s')\
        or (user_choice=='p'and com_choice=='r')\
        or (user_choice=='s'and com_choice=='p'):
        
        print("you won")

    else:
        print("you lost")
    should_continue=input("want to continue?,y/n").lower()
    
    if should_continue=="n":
        print("thanks for playing")
        break