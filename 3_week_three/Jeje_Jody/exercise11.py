#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# add code to print a line of hyphens the same length as the Belgium string

length_of_Belgium = len(Belgium)
print(length_of_Belgium)
print(length_of_Belgium * '-')

# followed by the string with the comma separators replaced by colons ':'
print(Belgium.replace(',', ':'))

# followed by the population of Belgium (the second field) plus the population of the capital city (the fourth field)
# Hint: the answer should be 11183818.

# belgium_population = Belgium[8:16]
# print(belgium_population)
# brussels_population = Belgium[27:32]
# print(brussels_population)
# total_population = int(belgium_population) + int(brussels_population)
# print(total_population)

# split is turning one long string into a list, and separating with the ,
belgium_list = Belgium.split(',')
print(belgium_list)
# use int to convert to integer to add
print(int(belgium_list[1]) + int(belgium_list[3]))




