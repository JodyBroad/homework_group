import sys
print (sys.platform) #sys is a built-in python module. We are importing it.
count_of_arguments = len(sys.argv)
# We are creating a variable called count_of_arguments and have assigned the len function to this variable.
# The function len() is one of Python's built-in functions. It returns the length of an object. For example, it can return the number of items in a list.
# argv is an argument vector - list of parameters or vectors. argument is a name we give to parameters.
#vector is a list. list of parameters to python scrips when we are running or executing our python script. The 0 parameter that we pass is the actual name of the script itself, title.
if count_of_arguments > 1:
    #conditonal statement with integer. len fucntion is working out the length and assigning to argc variable. it is 1 no greater than 1.
    print('Too many args')
    print('arg 1 is ' + sys.argv[1])
    print('arg 2 is ' + sys.argv[2])
#jumps to else block instead as is equal to 1, not greater than 1. There is only one argument. First argument is the script 0 argument.
else:
    where = 'World'
    print("Hello", where) #two argments to the print function, separated by commas. concatinate - glues them rtogther into one tring.
#single argment which is an expression. string says goodbye from. the + is another way to concatinate explicitly.
print('Goodbye from ' +#if 2 strings , ie text it will be the concatinate operator. if they were numbers then it would act as a plus sign.
      sys.argv [0])# sys.argv is list of arguments that has been passed to python as part of python script. file name is always 0 argument in vector.
#how we pass in our arguments - copy file path from run, go to terminal type in python (space) then paste file path in from /Users/, to add another argument type another space then the next argument for eg Christelle.