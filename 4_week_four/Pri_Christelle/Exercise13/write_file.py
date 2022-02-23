infile = open('Pelican.txt', 'w') #open file for append, create if it does not exist
infile.write('A wonderful bird is the pelican, \n')
infile = open('Pelican.txt', 'a')
infile.write('His bill holds more than his belican. \n')
lines = ['He can take in his beak,' '\n', 'Enough food for a week,''\n', 'But I’m damned if I see how the helican.' '\n']
infile.writelines(lines)

# the '\n' indicates that the line ends here and the remaining characters would be displayed in a new line.

