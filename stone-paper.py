from cgi import print_directory
import random

loop = True
user_count = 0
comp_count = 0 

while loop:
    user = int(input("For rock press 1\nFor paper press 2\nFor scissor press 3\n\n"))
    comp = random.randint(1,3)
    if (user==comp):
        print("Both Selected the same \n **Match Tie**")
    elif user==1 and comp==2:
        print("You select ROCK\nComputer select PAPER\n-----##You Lose!##-----")
        print("\n")
        comp_count=comp_count+1
    elif user==2 and comp ==1:
        print("You select PAPER\nComputer select ROCk\n-----$$You Won!$$-----")
        print("\n")
        user_count=user_count+1
    elif user==1 and comp==3:
        print("You select PAPER\nComputer select SCISSOR\n-----$$You Won!$$-----")
        print("\n")
        user_count=user_count+1
    elif user==3 and comp==1:
        print ("You select SCISSOR\nComputer select ROCK\n-----##You Lose!##-----")
        print("\n")
        comp_count=comp_count+1
    elif user==2 and comp==3:
        print("You selectPAPER\nComputer select SCISSOR\n-----##You Lose!##-----")
        print("\n")
        comp_count=comp_count+1
    elif user==3 and comp==2:
        print("You select SCISSOR\nComputer select PAPER\n-----$$You Won!$$-----")
        print("\n")
        user_count=user_count+1
    else:
        print("invalid")
    print("SCORE\nPLAYER SCORE:",user_count,"COMPUTER SCORE:",comp_count)
    print("\n")
    # play_again=input("You Wannaa Play Again Press y/n : ")
    if user_count==3 or comp_count ==3 :
        loop = False
print("----------GAME OVER----------")
    






