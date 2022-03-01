# rock, paper, scissors game

# three stages - 1 - get user input, convert it to Rock Paper Scissors
# 2 - generate computer action, convert it to Rock Paper Scissors
# 3 - compare the two and declare a winner

# we will need to generate random numbers later so:
import random

# scoring variables

human_victories = 0
computer_victories = 0

# list of possible actions
actions = ["Rock", "Paper", "Scissors"]

# doing a while loop allows us to play more than one game
while True:
    # prompt user to enter a value: R, P or S
    player_1 = input("Please select your fighter: R = Rock, P = Paper, S = Scissors: ")

# convert this input into Rock, Paper or Scissors

    def convert_player_1(player_1):
        if player_1.upper() == "R":
            player_1_choice = "Rock"
        elif player_1.upper() == "P":
            player_1_choice = "Paper"
        elif player_1.upper() == "S":
            player_1_choice = "Scissors"
        else:
            player_1_choice = "Invalid input"

        return player_1_choice


    player_1_action = convert_player_1(player_1)

    # to cover invalid input scenario
    if player_1_action == "Invalid input":
        print("Please enter a valid input, R, P or S")
        continue

    print("You chose: ", player_1_action)

    # generate a random value between 0 and 2 and use this to choose from the action list
    player_2_action = actions[random.randint(0, 2)]
    print("The computer chose: ", player_2_action)

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
