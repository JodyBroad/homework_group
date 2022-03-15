class Person:

    # Constructor
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.__address = "None"
        self._email = "None"

    def set_full_name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_firstname(self):
        return self._first_name

    def get_surname(self):
        return self._last_name

    def get_full_name(self):
        return self._first_name + " " + self._last_name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

    def __str__(self):
        return "Full name: " + self.get_full_name()


