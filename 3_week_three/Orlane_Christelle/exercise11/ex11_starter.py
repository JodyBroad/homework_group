#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
#print('-' * len(Belgium))


#print("Belgium", "10445852", "Brussels", "737966", "Europe", "1830", "Euro", "Catholicism", "Dutch", "French", "German", sep=':')

#field_2 = 10445852
#field_4 = 737966
#print("The population of Belgium added to the population of Brussels is:", field_2 + field_4)

Belgium_as_list = Belgium.split(',')
print(int(Belgium_as_list[1]) + int(Belgium_as_list[3]))

#Belgium_list = [10445852, 737966]
#print(sum(Belgium_list))
