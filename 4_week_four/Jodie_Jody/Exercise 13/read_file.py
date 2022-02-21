# opening and reading to slurp the entire contents

limerick = open("pelican.txt")
# checking the file type - this is the file handle
print(type(limerick))
# printing metadata, not the contents
print(limerick)

# to print entire thing - slurping, need to use read method
print("The Limerick using the read method:")
print(limerick.read())

# create a new list, and then add each line as a new item
limerick_list = open("pelican.txt").readlines()
# print(limerick_list)
# checking the length of the list and printing it
print("Print the number of items in the list: ", len(limerick_list))

# this prints each item from the list we made above
print("The Limerick from the list: ")
for limerick_lines in limerick_list:
    # remove blank lines with end =""
    print(limerick_lines, end="" )

# this is printing directly from the text file - this is the most efficient way
print("The Limerick from the txt file: ")
for limerick_lines in open("pelican.txt"):
    # remove blank lines with end =""
    print(limerick_lines, end="" )