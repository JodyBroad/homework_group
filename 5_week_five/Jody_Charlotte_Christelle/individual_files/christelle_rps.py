# Need to first import random and create any functions needed for the game
# Establish variables to track wins for the player and the computer
# Get input from user to choose Rock, Paper or Scissors
# The computer selects at random Rock, Paper, or Scissors
# If loop - this needs to compare player selection and computer selection, and then determine who won or if it is a tie. This loops also needs to track wins and print results and then ask the player if they would like to continue the game.

import random  # random is a built-in python module


def convert_rps():  # here I have created a function that converts R, P, or S from the user inputs into 'You are Rock', 'You are Paper' etc. I will then call on this function later on in the code.

    if player_choice == 'R':
        print("You are Rock")
    elif player_choice == 'P':
        print("You are Paper")
    elif player_choice == 'S':
        print("You are Scissors")
        return


print("Rock, Paper Scissors Game - let's play!")

print("R = Rock, P = Paper, S = Scissors")
print("Rock smashes Scissors, Paper wraps Rock and Scissors cut Paper!")

# I have wrapped this entire secton around a while loop, this enables the player to choose whether to keep playing or not.
while True:
    player_choice = str(input("Enter R, P or S: "))
    convert_rps()
   


    possible_choices = ["Rock", "Paper", "Scissors"]  # list of possible choices that the computer will choose from at random using the random.choice method below
    computer_choice = random.choice(possible_choices)
    print("Computer chooses", computer_choice)
    # below is an if loop which compares the computer's choice to the player's choice that they have input.
    if computer_choice == 'Rock' and player_choice == 'P':
        print("You win!")
    elif computer_choice == 'Paper' and player_choice == 'S':
        print("You win!")
    elif computer_choice == 'Scissors' and player_choice == 'R':
        print("You win!")
    elif computer_choice == 'Paper' and player_choice == 'R':
        print("You lose!")
    elif computer_choice == 'Scissors' and player_choice == 'P':
        print("You lose!")
    elif computer_choice == 'Rock' and player_choice == 'S':
        print("You lose!")
    else:
        print("It's a tie")

    play_again = input("Do you want to continue playing? Please enter y/n: ").lower()
    if play_again == "n":
        break
    else:
        continue


