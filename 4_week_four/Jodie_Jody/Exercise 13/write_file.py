# create file handle to open and append to file called pelican.txt

# 'a' will append (keep adding), w will overwrite each time

file_handler = open("pelican.txt", 'w')
# adding first line to the file
file_handler.write("A wonderful bird is the pelican, \n")
# adding second line using write method
file_handler.write("His bill holds more than his belican, \n")
# creating list with additional lines
# need to add \n for linebreaks
lines = ["He can take in his beak, \n", "Enough food for a week,  \n", "But I'm damned if I see how the helican. \n"]
file_handler.writelines(lines)

# good practice to close the file afterwards
file_handler.close()