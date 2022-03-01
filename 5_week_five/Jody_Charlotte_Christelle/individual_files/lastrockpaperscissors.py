import random

choices = ["Rock", "Paper", "Scissors"]
# user_input = input("Enter a value, R, P, or S\n")
# global user_input_choice
# global computer_input_choice


def convert_user_input():
    user_input = input("Enter a value, R, P, or S\n").upper()
    global user_input_choice
    # user_input.upper()
    # user_input = user_input.upper()
    if user_input == "R":
        user_input_choice = choices[0]
        return "You chose {}".format(user_input_choice)
    elif user_input == "P":
        user_input_choice = choices[1]
        return "You chose {}".format(user_input_choice)
    elif user_input == "S":
        user_input_choice = choices[2]
        return "You chose {}".format(user_input_choice)
    else:
        return "You have entered an incorrect value, try again"


# convert_user_input()
# print(user_input_choice)
print(convert_user_input())

# user_input_choice = convert_user_input()
# print(str(user_input_choice))

# computer_input = random.randint(0, 2)


def convert_computer_input():
    # global computer_input
    global computer_input_choice
    computer_input = random.randint(0, 2)
    if computer_input == 0:
        computer_input_choice = choices[0]
        return "The computer chose {}".format(computer_input_choice)
    if computer_input == 1:
        computer_input_choice = choices[1]
        return "The computer chose {}".format(computer_input_choice)
    if computer_input == 2:
        computer_input_choice = choices[2]
        return "The computer chose {}".format(computer_input_choice)


# convert_computer_input()
# print(computer_input_choice)
print(convert_computer_input())


def who_wins(user_input_choice, computer_input_choice):
    # global user_input_choice
    # global computer_input_choice
    if user_input_choice == computer_input_choice:
        print("Both players selected the same, it is a tie")
    elif user_input_choice == "Rock":
        if computer_input_choice == "Scissors":
            print("Rock smashes scissors, so you win")
        else:
            print("Paper wraps Rock, you lose")
    elif user_input_choice == "Paper":
        if computer_input_choice == "Rock":
            print("Paper wraps rock, so you win")
        else:
            print("Scissors cut paper, so lost")
    elif user_input_choice == "Scissors":
        if computer_input_choice == "Paper":
            print("Scissors cut paper, so you win")
        else:
            print("Rock smashes scissors, so you lose")


who_wins(user_input_choice, computer_input_choice)
# user_input_choice = convert_user_input(user_input)
# computer_input_choice = convert_computer_input()

# who_wins(user_input, computer_input)


# if __name__ == '__lastrockpaperscissors__':
#     print(convert_user_input(), convert_computer_input())




# who_wins(user_input_choice, computer_input_choice)
# print(convert_user_input())
# print(convert_computer_input())
# "You chose {}".format(choices[2])