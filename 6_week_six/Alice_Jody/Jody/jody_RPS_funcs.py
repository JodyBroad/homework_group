import datetime

# list of possible actions

actions = ["Rock", "Paper", "Scissors"]


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


def who_wins(human_action, computer_action):
    global winner
    if human_action == computer_action:
        print("Both players selected the same, it is a tie")
        winner = "Tie"
    elif human_action == "Rock":
        if computer_action == "Scissors":
            print("Rock breaks scissors, so you are victorious!")
            winner = "Human"
            return winner
        else:
            print("Paper wraps rock, so you have been defeated")
            winner = "Computer"
            return winner
    elif human_action == "Paper":
        if computer_action == "Rock":
            print("Paper wraps rock, so you are  victorious!")
            winner = "Human"
            return winner
        else:
            print("Scissors cut paper, so you have been defeated")
            winner = "Computer"
            return winner
    elif human_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cut paper, so you are victorious!")
            winner = "Human"
            return winner
        else:
            print("Rock breaks scissors, so you have been defeated")
            winner = "Computer"
            return winner


# can't get this to work here because it needs to import the variables from the other file
# def scoreboard():
#     current_time = datetime.datetime.now()
#     dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
#     score_file = open("scores.txt", 'a')
#     # from homework_week_six.jody_RPS import player_name, human_victories, computer_victories
#     score_file.write(dt_string + "     " + f"{str(player_name) : <35}" + "human victories: " + str(human_victories) +
#                      "     " + "computer victories: " + str(computer_victories))
#     score_file.write("\n ------------------------------------------------------------------------------------------"
#                      "----------------------------- \n")
#     score_file.close()

# def main():
# I don't really have anything to put in here, but would put any executable code in here

# so if this file is the __main__ one it will run all the executable code, but if it is imported elsewhere it won't
# run this code
# if __name__ == "__main__":
#   main()
