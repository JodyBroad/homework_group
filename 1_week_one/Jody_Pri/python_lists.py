# creates list of cheeses called cheese
cheese = ['cheddar', 'stilton', 'cornish yarg']
# will print the cheese in position 1 (2nd on the list as we start from 0)
print(cheese[1])
# last item on the list [-1] is therefore popped off, changing this number will change the position it moves to
# if we change to [-2] then stilton gets replaced
cheese[-1] = 'red leicester'
# print cheese list
print(cheese)
# this is a three item list - position [1] is the list ['camembert', 'brie'] of which position [0] is camembert
cheese = ['cheddar', ['camembert', 'brie'], 'stilton']
print(cheese[1][0])
