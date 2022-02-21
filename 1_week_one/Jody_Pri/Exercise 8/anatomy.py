# Example Python script
# this is importing built in python module sys
import sys
# declaring argc as a variable which is equal to the function len - checking the length of the value of sys and the
# value of argv (script pathname) [0] is the filename when 0 is passed
# sys.argv is The list of command line arguments passed to a Python script
# argv is an argument vector - the list of parameters that have been passed to this script
count_of_arguments = len(sys.argv)
# conditional statement; if count_of_arguments is larger than one, print "too many args"
if count_of_arguments > 1:
    print('Too many args')
    print('arg 1 is ' + sys.argv[1])
    print('arg 2 is ' + sys.argv[2])
# else, if less than or equal to 1, then the variable where is equal to world, so will print "Hello world"
else:
    where = 'World'
    print("Hello", where)
# printing goodbye from the file pathway of the project which will print regardless of the conditional statement
# the file name is always the 0th argument passed to a script
print('Goodbye from ' +
      sys.argv[0])
# parameters were passed in via terminal - copy the filepath from the output, go into terminal and then type "python
# filepath and then any other arguments you want to pass in