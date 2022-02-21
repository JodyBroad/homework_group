import random

# lotto_numbers = []
# print(type(lotto_numbers))
# number_1 = random.randint(1, 50)
# print(number_1)
#
# lotto_numbers.append(number_1)
# print(lotto_numbers)

# could have used set to not have any duplicates, then wouldn't need the extra code below
# could also have just done a while loop, while len <6 for the main loop

#for i in range(0, 6):
    #number = random.randint(1, 50)
    # to get rid of duplicates
   # while number in lotto_numbers:
       # number = random.randint(1, 50)
        # if it isn't already on the list, we now add it to the list with append
    #lotto_numbers.append(number)
# print(lotto_numbers)

#list numbers sorted
# lotto_numbers_sorted = sorted(lotto_numbers)
# print("This week's lottery numbers are: ", lotto_numbers_sorted)


lotto_numbers = set()
# print(type(lotto_numbers))

while len(lotto_numbers) < 6:
    number = random.randint(1, 50)
    lotto_numbers.add(number)
print(lotto_numbers)

#list numbers sorted
lotto_numbers_sorted = sorted(lotto_numbers)
print("This week's lottery numbers are: ", lotto_numbers_sorted)