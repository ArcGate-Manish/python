import random
from wsgiref.util import guess_scheme
guess=random.randint(1,10)
# print(guess)

game = True
won=3

while game:
    player=int(input("Enter a number of your choice : \n"))
    if player==guess:
        print("You Guess RIGHT Number\n-------YOU WON-------")
        won=won-1
    elif player<guess:
        print("You Guess WRONG Numbern\n **The number you guess is smaller** ")
        won=won-1
    elif player>guess:
        print("You Guess WRONG Number\n **The number you guess is greater** ")
        won=won-1
    else:
        print("# Invalid Response #")
    
    if won==0:
        print("......YOU LOST!......")
        game=False
    



