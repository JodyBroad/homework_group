class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def show(self):
        print(f"{self.name} is {self.age} and lives in {self.location}")