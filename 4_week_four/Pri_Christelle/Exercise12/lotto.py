import random
#Generate 6 random numbers between 1 and 50
randomlist = random.sample(range(1, 50), 6)#creates a variable of randomlist. random. is in-built module of Python which is used to generate random numbers. sample is a method in python.
print(randomlist)
#or - neater code
print(random.sample(range(1, 50), 6))

#a Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
# while loops can continue endlessly

import random
s=set()
for i in range(6):
    s.add((random.randint(1,50)))
print('The winning lotto numbers are:', s)







