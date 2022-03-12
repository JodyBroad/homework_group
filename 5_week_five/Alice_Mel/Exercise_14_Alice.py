# updated post Monday session with Victoria


# creating function to convert user input - 'R', 'P' or 'S' - into 'Rock', 'Paper' or 'Scissors'
def convert_user_input(user_input_letter):
    if user_input_letter == 'R':
        user_selection = 'Rock'
    elif user_input_letter == 'P':
        user_selection = 'Paper'
    else:
        user_selection = 'Scissors'
    return user_selection
# is it not a problem that this function uses variable names?


# creating a function to generate a random number between 0 and 2 and convert it to 'Rock', 'Paper', or 'Scissors'
def generate_computer_selection():
    import random
    options = ['Rock', 'Paper', 'Scissors']
    random_number = random.randint(0, 2)
    return options[random_number]


# removed this function, as combined with above
# creating function to convert computer number - 0, 1, or 2 - into 'Rock', 'Paper' or 'Scissors'
# def convert_computer_number(computer_choice):
#     if computer_choice == 0:
#         computer_selection = 'Rock'
#     elif computer_choice == 1:
#         computer_selection = 'Paper'
#     else:
#         computer_selection = 'Scissors'
#     return computer_selection


# creating a function to determine win, loss or draw:
# grouped all win and lose situations together for ease of reading
def determine_game_outcome(user, computer):
    if user == computer:
        outcome = 'D'
    elif user == 'Rock' and computer == 'Scissors':
        outcome = 'W'
    elif user == 'Paper' and computer == 'Rock':
        outcome = 'W'
    elif user == 'Scissors' and computer == 'Paper':
        outcome = 'W'
    elif user == 'Rock' and computer == 'Paper':
        outcome = 'L'
    elif user == 'Paper' and computer == 'Scissors':
        outcome = 'L'
    else:
        outcome = 'L'
    return outcome


# STEP 1 - user input: R, P, or S
accepted_user_inputs = ['R', 'P', 'S']

user_input = None
while user_input not in accepted_user_inputs:
    user_input = input('Please enter R, P, or S: ').upper()
    # REVISIT: can't get this while loop to work without printing error message
    # print('You have not entered an accepted letter, please try again.')

# STEP 2 - convert user input to 'Rock', 'Paper' or 'Scissors'
user = convert_user_input(user_input)
print('You have selected: ', user)

# STEP 3 - generate computer selection:
computer_choice = generate_computer_selection()
print('Computer has selected: ', computer_choice)

# STEP 4 - compare user input and computer number to determine outcome of game:
game_outcome = determine_game_outcome(user, computer_choice)

win_message = "You win!"
lose_message = "You lose!"
draw_message = "You draw!"

if game_outcome == 'W':
    print(win_message)
elif game_outcome == 'L':
    print(lose_message)
else:
    print(draw_message)







