# rock paper scissors game

import random

print("Rock, Paper Scissors Game - let's play!\nThe rules are: Rock smashes Scissors, Paper wraps Rock and Scissors cut Paper!" )

# list of possible actions
actions = ["Rock", "Paper", "Scissors"]

# scoring variables
human_victories = 0
computer_victories = 0

while True:
    player_1 = input("Please select your fighter: R = Rock, P = Paper, S = Scissors: ")

    def convert_player_1(player_1):
        if player_1.upper() == "R":
            player_1_choice = actions[0]
        elif player_1.upper() == "P":
            player_1_choice = actions[1]
        elif player_1.upper() == "S":
            player_1_choice = actions[2]
        else:
            player_1_choice = "Invalid input"

        return player_1_choice

# calling convert_player_1 and saving the output to the variable player_1_action
    player_1_action = convert_player_1(player_1)

    # to cover invalid input scenario
    if player_1_action == "Invalid input":
        print("Please enter a valid input, R, P or S")
        continue

# printing what the player chose
    print("You chose: {}".format(player_1_action))

# function to convert computer input
    def convert_computer_input(computer_input):
        if computer_input == 0:
            computer_input_choice = actions[0]
            return computer_input_choice
        elif computer_input == 1:
            computer_input_choice = actions[1]
            return computer_input_choice
        elif computer_input == 2:
            computer_input_choice = actions[2]
            return computer_input_choice

# generating random number for computer input
    computer_input = random.randint(0, 2)
    player_2_action = convert_computer_input(computer_input)
    print("The computer chose: {}".format(player_2_action))


   # compares user's choice against computer's choice and then display a message as to if the user won, lost or drew
    # if I do this as a function the scoring doesn't work

    if player_1_action == player_2_action:
        print("Both players selected the same, it is a tie")
    elif player_1_action == "Rock":
        if player_2_action == "Scissors":
            print("Rock breaks scissors, so you are victorious!")
            human_victories += 1
        else:
            print("Paper wraps rock, so you have been defeated")
            computer_victories += 1
    elif player_1_action == "Paper":
        if player_2_action == "Rock":
            print("Paper wraps rock, so you are victorious!")
            human_victories += 1
        else:
            print("Scissors cut paper, so you have been defeated")
            computer_victories += 1
    elif player_1_action == "Scissors":
        if player_2_action == "Paper":
            print("Scissors cut paper, so you are victorious!")
            human_victories += 1
        else:
            print("Rock breaks scissors, so you have been defeated")
            computer_victories += 1

    print("Total human victories = ", human_victories, "Total computer victories = ", computer_victories)

# ask them if they want to play again, any input other than Y/y will break the loop and exit

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() != "Y":
        break

