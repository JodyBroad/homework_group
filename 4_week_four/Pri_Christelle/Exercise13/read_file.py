#opens the file Pelican.txt
infile = open('Pelican.txt').read() #slurps the entire contents of your pelican.txt file
print(type(infile))#prints the data type of the output
print(infile)#prints the contents of returned data

infile = open("Pelican.txt", "r")
content_list = infile.readlines() #makes the Pelican.txt file into a list?
print(content_list)

#content = infile.read()
#content_list = content.split(",")
#print(content_list)

print(len(content_list))#the ouput will be the number of items in the list

# iterate over the lines in a file:
with open('Pelican.txt', "r") as a_file:
  for line in a_file:#this reads each line once

    stripped_line = line.strip()#remove characters or white spaces from the beginning or end of a string
    print(stripped_line)

