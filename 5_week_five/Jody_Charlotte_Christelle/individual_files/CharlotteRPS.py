# You are going to create a command line version of the game: Rock, Paper, Scissors
# The user will play against the computer at this game.
# You should design a program that does the following:
# prompts the user to enter a value: R, P or S
# The program should convert this value into Rock, Paper, or Scissors respectively
# Asks the computer to generate a random value between 0 and 2
# Compare the user's choice with the computer's choice to display a message indicating whether the user won, lost or drew against the computer
# Showcase what you have learned about conditional statements and create your own functions

# Rock smashes Scissors, Paper wraps Rock, Scissors cut Paper!

# My thoughts
# When prompting the user to enter a value: R, P or S:
    # Need to convert the user input to upper
    # Need to ensure that user only inputs the correct data type & value; display message if incorrect entry.
    # Does this need to be a loop? look back at PIN exercise
    # Don't necessarily need to return the code to the user?
    # Can print "You are ....".

# Could have variables for each round? round_1, round_2, round_3
# Could have variables for user_input, computer_input
# the computer_input is the random.randint(0, 2) function
# How many functions needed?
        #1. Function that converts user input into Rock, Paper, or Scissors
        #2. Function that converts computer's choice into Rock, Paper, or Scissors
        #3. Function that compares the user's choice with the computer's choice to display
            #a message indicating whether the user won, lost or drew against the computer.

# The game should run three times (three rounds), so need a for loop (because know the number of times to run the code)
# Think about which variables need to be global and local
# Could either assign values to Rock (0), Paper (1), Scissors (2) as a global variable
# Could create a user_list (user score) of empty values and each round += value to the list.
# Could create a computer_list (computer score) of empty values and each round += value to the list
# At the end could have a function which compares these two scores

# Different combinations for each round:               Function names
# Rock, Rock                No winner                          nothing_happens
# Rock, Scissors            Rock smashes Scissors      smash  rock_smashes_scissors
# Scissors, Scissors        No winner                           nothing_happens
# Rock, Paper               Paper wraps Rock           wrap     paper_wraps_rock
# Paper, Paper              No winner                           nothing_happens
# Scissors, Paper           Scissors cut Paper         cuts     scissors_cut_paper

# Possible outcomes
# User wins & computer loses           The user and computer can't both win
# Computer wins & user loses
# User & computer draw                 Neither the user nor computer wins

# I might want to pass a list as an argument

#def play_game(smash, wrap, paper):

# Ask the user to enter a value: R, P or S
# Ensure that user can only input R, P or S, if provide different data type/string then print/return message & ask again.

# user_input = input("Enter a value: R, P or S ")
# if user_input.upper() == 'R':
#     print('You are Rock')
# if user_input.upper() == 'P':
#     print('You are Paper')
# if user_input.upper() == 'S':
#     print('You are Scissors')
# else:
#     print("You did not enter a value correctly, try again")

# user_input = input("Enter a value: R, P or S ")
user_input_scores_list = []


# def convert_user_input(user_input_value):
#     user_input = input("Enter a value: R, P or S ")
#     converted_user_input_to_rock = user_input.upper() + 'ock'
#     converted_user_input_to_paper = user_input.upper() + 'aper'
#     converted_user_input_to_scissors = user_input.upper() + 'cissors'
#     if user_input.upper() == 'R':
#         return converted_user_input_to_rock
#     if user_input.upper() == 'P':
#         return converted_user_input_to_paper
#     if user_input.upper() == 'S':
#         return converted_user_input_to_scissors


# print("Your choice is", convert_user_input(0))
# # user_choice = convert_user_input(0)

def convert_user_choice_(letter_value, user_choice_message='Your choice is'):
    user_letter_input = input("Enter a value: R, P or S ")
    user_choice = user_letter_input.upper()
    if user_choice == 'R':
        print(user_choice_message, "Rock")
    if user_choice == 'P':
        print(user_choice_message, "Paper")
    if user_choice == 'S':
        print(user_choice_message, "Scissors")


# print(convert_user_choice_(0))



# Computer to generate a random value between 0 and 2.
import random
computer_input = random.randint(0, 2)

# Convert the computer's choice.
# if each value multiplied by 1 is 0, 1 or 2 as the output, then do this
# Could have a multiply function that converts computer value to Rock, Paper, Scissors by
# 0 x 1 = 'Rock'
# 1 x 1 = 'Paper'
# 2 x 1 = 'Scissors'

# Created a function called convert_computer_choice with the arguments value and multiply_by_1.


def convert_computer_choice(value, multiply_by_1):
    multiply_by_1 = (computer_input * 1)
    if multiply_by_1 == 0:
        return 'Rock'
    if multiply_by_1 == 1:
        return 'Paper'
    if multiply_by_1 == 2:
        return 'Scissors'


# convert_computer_choice(computer_input, 1)
computer_choice = convert_computer_choice(computer_input, 1)
print("The computer's choice is", computer_choice)

def convert_computer_choice(value, multiply_by_1):
    multiply_by_1 = (computer_input * 1)
    if multiply_by_1 == 0:
        return 'Rock'
    if multiply_by_1 == 1:
        return 'Paper'
    if multiply_by_1 == 2:
        return 'Scissors'




# created a function called convert_choice, which multiplies the user value by one.
# The answer returns either Rock, Paper, or Scissors
# def convert_choice(user_value, multiply_by_1):
#     multiply_by_1 = (user_value * 1)
#     if multiply_by_1 == 0:
#         return 'Rock'
#     if multiply_by_1 == 1:
#         return 'Paper'
#     if multiply_by_1 == 2:
#         return 'Scissors'

# Might have to have a function that adds to the respective user & computer scores
# Defining functions for the actions
# Might need to change the strings to variables


# def smashes(value):
#     if user_input == 'Rock' and computer_input == 'Scissors':
#         return "Rock smashes Scissors"
#     if user_input == 'Scissors' and computer_input == 'Rock':
#         return "Rock smashes Scissors"
#
#
# def wraps(value):
#     if user_input == 'Paper' and computer_input == 'Rock':
#         return "Paper wraps Rock"
#     if user_input == 'Rock' and computer_input == 'Paper':
#         return "Paper wraps Rock"
#
#
# def cuts(value):
#     if user_input == 'Scissors' and computer_input == 'Paper':
#         return "Scissors cut Paper"
#     if user_input == 'Paper' and computer_input == 'Scissors':
#         return "Scissors cut Paper"
#
#
# def nothing_happens(value):
#     if user_input == computer_input:
#         return "Nobody scores points this round"
#

# print(smashes())
# print(wraps())
# print(cuts())
# print(nothing_happens())

# Figuring out the logic
# if user_input is the same as the computer_input, do nothing, add 0.
# if someone wins, add 3 to winner score.

# Conditional expressions
# Rock = 0
# Paper = 1
# Scissors = 2
# print ("Rock smashes Scissors") if
# answer = Rock + (3 if Rock < Paper else 0)
#


max_number_of_rounds = 3
round_number = 0


# while round_number < max_number_of_rounds:
#




# import math
#
# def play_best_of(n):
#    player_wins = 0
#    computer_wins = 0
#    wins_necessary = math.cell(n/2)


# for index, num in enumerate(user_input_scores_list):
#     if num > 3: user_input_scores_list[0] += 1
#
#
# for index, num in enumerate(user_input_scores_list):
#     if user_
#


# Display messages
# "You lost! Better luck next time"
# "You drew with the computer!"
# "You won! Congratulations"