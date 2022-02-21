import random

# value = random.randint(1, 50)
# print(value)

#puts all numbers in the range of 1 -50 in a list
numbers = list(range(1, 50))
# print(numbers)
# to shuffle numbers can use random.shuffle

#random.sample will select unqiue values from the list, the k argument specifics how much values you wish to select
lotto = random.sample(numbers, k=6)
print(lotto)