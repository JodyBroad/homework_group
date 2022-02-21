cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke' this is trying to add Oke at the end of the list, but has not put the sqaure brackets so its adding it as individual letters instead of a word
cheese += ['Oke']
#this is now adding Oke at the end of string as list item rather than individual letters
print(cheese)

# to add two new cheeses to the list in a single command
cheese += ['Edam', 'Swiss']
cheese.extend(['Gorgonzola', 'Brie'])
print(cheese)

#Question 2

tup = 'Hello'
print(len(tup))
print(type(tup))
#this will print 5
#this is counting it as string data so its counting the individual letters


tup = 'Hello',
print(len(tup))
print(type(tup))
#this will print 1
#tuple is a comma seperated list. This will count the items of the variable


