import random
victor = False ### SRC - I think the variable should be called game_over
choices = ["rock","paper","scissors"]
while not victor:
    user_choice = input("enter your move: ") ### SRC - It's not clear what I need to enter!
    ### SRC - This should be a while rather than an if...
    if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        print("valid move")
    else:
        user_choice = input("invalid move enter again: ")
    #end if
    computer_choice = random.choice(choices)
    print(computer_choice)
    if user_choice == computer_choice:
        print("draw")
    elif user_choice == "rock" and computer_choice == "paper" or user_choice == "scissors" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "rock":
        print("you won")
    else:
        print("you lost")
    #end if
    ans = input("do you want to play again? (Y/N)")
    if ans == 'n' or ans == 'N': 
        victor = True
    #end if
#end while
