import jody_RPS_funcs, random, datetime

print(f"{'***Rock, Paper, Scissors - let battle commence!***' : ^100}")
print(f"{'***The rules are: Rock smashes Scissors, Paper wraps Rock and Scissors cut Paper!***' : ^100}")
print("*************************************************************************************************************")

# list of possible actions
actions = ["Rock", "Paper", "Scissors"]

# scoring variables
human_victories = 0
computer_victories = 0

player_name = input(f"{'Enter your name puny human : ' : <65}")


while True:
    human = input(f'{"Please select your fighter: R = Rock, P = Paper, S = Scissors: " : <65}')

# calling convert_player_1 and saving the output to the variable player_1_action
    human_action = jody_RPS_funcs.convert_human(human)

    # to cover invalid input scenario
    if human_action == "Invalid input":
        print("Please enter a valid input, R, P or S")
        continue

# printing what the player chose
    print(
        "*************************************************************************************************************")
    print("You chose: {}".format(human_action))

# generating random number for computer input
    computer_input = random.randint(0, 2)
    computer_action = jody_RPS_funcs.convert_computer_input(computer_input)
    print("The computer chose: {}".format(computer_action))
    print(
        "*************************************************************************************************************")

# compares user's choice against computer's choice and then display a message as to if the user won, lost or drew

    jody_RPS_funcs.who_wins(human_action, computer_action)
    if jody_RPS_funcs.winner == "Human":
        human_victories += 1
    elif jody_RPS_funcs.winner == "Computer":
        computer_victories += 1

    print("Total human victories = ", human_victories, "Total computer victories = ", computer_victories)
    print(
        "*************************************************************************************************************")

# ask them if they want to play again, any input other than Y/y will break the loop and exit

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() != "Y":
        # can't get this to work as a function in the other file as it needs the variables in here,
        # importing them into the _funcs files causes problems
        current_time = datetime.datetime.now()
        dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
        score_file = open("scores.txt", 'a')
        # from homework_week_six.jody_RPS import player_name, human_victories, computer_victories
        score_file.write(
            dt_string + "     " + f"{str(player_name) : <35}" + "human victories: " + str(human_victories) +
            "     " + "computer victories: " + str(computer_victories))
        score_file.write("\n ------------------------------------------------------------------------------------------"
                         "----------------------------- \n")
        score_file.close()
        break
