# PIN numbers extra
# Joint - Jody & Isabel

import getpass

# with get pass you need to add prompt= before then input prompt
# open this in terminal
# terminal will not display input values with asterisk but instead will be blank
# if you complete the program, then re-enter the file 'pin_numbers_extra.py' to run other options.

# putting the number in "" means it is already a string, so we can match it with the input
pin_number = "1234"
# attempt needs to start at 0 as we are using as a counter
attempt = 0
# max_attempts can then be amended if we want to change the number of attempts allowed
max_attempts = 3


while attempt <= max_attempts:
    supplied_pin = getpass.getpass(prompt="Enter your PIN: ")
    if supplied_pin == pin_number:
        print("Congratulations you win access to your own money! ")
        # success condition, so can end the loop
        break
    else:
        attempt += + 1
        if attempt < max_attempts -1:
            print("That is incorrect, please try again, your next try will be attempt number: ", attempt + 1)
            # final attempt message
        elif attempt == max_attempts - 1:
            print("That is incorrect, please try again, this is your final attempt: ", attempt +1 )
        else:
            if attempt >= max_attempts:
                print("You have reached the maximum number of attempts and you account is now locked")
             # failure condition met, so can exit the loop
                break

#