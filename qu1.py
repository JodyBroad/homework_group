cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']#this does not work correctly because the 'Oke' need to be in [] to append to the list.
print(cheese)

#or you could use this method, but only for one item:
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.append('Oke')
print(cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke']
cheese.extend(['Cambozola', 'Gouda'])
print(cheese)

#or can use this method to insert in different positions in the list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke']
cheese.insert(0, 'Cambozola')
print(cheese)
cheese[2:2] = ['Gouda', 'Mouldy cheese']# with [2:2] the first number means the entry point of the list item and the second item refers to the end index number of the list entries.
print(cheese)
cheese.remove('Mouldy cheese')
print(cheese)

#cheese.append('Tomato')
print(cheese)

cheese.insert(3, 'Tomato')
print(cheese)



