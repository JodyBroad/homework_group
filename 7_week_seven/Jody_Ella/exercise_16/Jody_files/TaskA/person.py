# this is going to be the superclass person, customer and employee are types of person so will be subclasses

# capital P for a class

class Person:
    # will keep track of how many have been created
    num_created = 0

    # constructor - anything we need to create our object; variables, details etc
    def __init__(self, first_name, surname):
        self.__first_name = first_name
        self.__surname = surname
        self.__full_name = first_name + ' ' + surname
        Person.num_created += 1

    def fullname(self):
        return '{}'.format(self.__full_name)

    # getter - reads data from inside the object
    # translation
    def get_person_name(self):
        return self.__full_name

    # setter - writes data
    # validation logic

    def set_person_name(self, first_name, surname):
        self.__full_name = first_name + ' ' + surname
