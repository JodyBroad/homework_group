import random


# function to define user 'player 1' move
def user_play():
    player1 = input('Will you play Rock (R), Paper (P) or Scissors (S)? \n').lower()
    if player1 == 'r':
        print(f'You have played Rock')
    elif player1 == 'p':
        print(f'You have played Paper')
    elif player1 == 's':
        print(f'You have played Scissors')
# else statement to catch errors - begin game again.
    else:
        print(f'Error, please enter R, P or S')
        game_play()
    return player1


# automated random game play function for player 2
def comp_play():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = choices[random.randint(0, 2)]
    print(f'The computer played {computer_choice}')
    return computer_choice


# define function to continue playing rounds of the game
def play_round():
    rounds = input('Do you want to play again? y/n? \n')
    if rounds == 'y':
        game_play()
    else:
        print(f'Thanks for playing!')


# function to determine outcome of the game
def game_play():
    user = user_play()
    comp = comp_play()

    if user == comp:
        print('Its a tie!')
    elif user == 'r' and comp == 'paper':
        print('You lose, paper has wrapped up your rock!')
    elif user == 'p' and comp == 'scissors':
        print('You lose, scissors have ripped through your paper')
    elif user == 's' and comp == 'rock':
        print('You lose, the rock has smashed up your scissors')
    else:
        print('Congratulations, You win!')
# call function to continue playing rounds
    play_round()


game_play()
