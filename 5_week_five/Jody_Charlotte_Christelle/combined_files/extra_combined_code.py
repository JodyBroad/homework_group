# rock paper scissors game

import random
import datetime

print("Rock, Paper Scissors Game - let's play!\nThe rules are: Rock smashes Scissors, Paper wraps Rock and Scissors cut"
      " Paper!")
player_name = input("Enter your name puny human: ")

# list of possible actions
actions = ["Rock", "Paper", "Scissors"]

# scoring variables
human_victories = 0
computer_victories = 0

# function for human choice


def convert_human(human):
    if human.upper() == "R":
        human_choice = actions[0]
    elif human.upper() == "P":
        human_choice = actions[1]
    elif human.upper() == "S":
        human_choice = actions[2]
    else:
        human_choice = "Invalid input"

    return human_choice

# function to convert computer input


def convert_computer_input(computer_input):
    computer_input_choice = actions[computer_input]
    return computer_input_choice

# function to decide winner and scoring


def who_wins(player_1_action, player_2_action):
    global human_victories
    global computer_victories
    if player_1_action == player_2_action:
        print("Both players selected the same, it is a tie")
    elif player_1_action == "Rock":
        if player_2_action == "Scissors":
            print("Rock breaks scissors, so", player_name, "is victorious!")
            human_victories += 1
        else:
            print("Paper wraps rock, so you have been defeated", player_name)
            computer_victories += 1
    elif player_1_action == "Paper":
        if player_2_action == "Rock":
            print("Paper wraps rock, so", player_name, "is victorious!")
            human_victories += 1
        else:
            print("Scissors cut paper, so you have been defeated", player_name)
            computer_victories += 1
    elif player_1_action == "Scissors":
        if player_2_action == "Paper":
            print("Scissors cut paper, so", player_name, "is victorious!")
            human_victories += 1
        else:
            print("Rock breaks scissors, so you have been defeated", player_name)
            computer_victories += 1


while True:
    human = input("Please select your fighter: R = Rock, P = Paper, S = Scissors: ")

# calling convert_player_1 and saving the output to the variable player_1_action
    human_action = convert_human(human)

    # to cover invalid input scenario
    if human_action == "Invalid input":
        print("Please enter a valid input, R, P or S")
        continue

# printing what the player chose
    print("You chose: {}".format(human_action))

# generating random number for computer input
    computer_input = random.randint(0, 2)
    computer_action = convert_computer_input(computer_input)
    print("The computer chose: {}".format(computer_action))

# compares user's choice against computer's choice and then display a message as to if the user won, lost or drew

    who_wins(human_action, computer_action)
    print("Total human victories = ", human_victories, "Total computer victories = ", computer_victories)

# ask them if they want to play again, any input other than Y/y will break the loop and exit

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() != "Y":
        current_time = datetime.datetime.now()
        dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
        score_file = open("scores.txt", 'a')
        score_file.write(dt_string + "     " + str(player_name) + "     " + "human victories: " + str(human_victories) +
                         "     " + "computer victories: " + str(computer_victories))
        score_file.write("\n -------------------------------------------------------------------------------------- \n")
        score_file.close()
        break
