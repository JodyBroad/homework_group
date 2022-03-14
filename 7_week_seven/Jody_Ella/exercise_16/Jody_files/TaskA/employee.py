# employee is subclass of person, so need to import
from person import Person


class Employee(Person):
    num_of_employees = 0

    # annual payrise as a class variable to allow you to update for all employees simultaneously
    annual_payrise = 1.05

    def __init__(self, first_name, surname, job_title, department, salary):
        super().__init__(first_name, surname)
        self.__job_title = job_title
        self.__department = department
        self.__salary = salary
        Employee.num_of_employees += 1

    def apply_payrise(self):
        self.__salary = (float(self.__salary) * float(self.annual_payrise))
        return self.__salary

    # getter - job title
    def get_job_title(self):
        return self.__job_title

    # setter - job title
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # getter - department
    # def get_department(self):
    #     return self.__department
    #
    # # setter - department
    # def set_department(self, department):
    #     self.__department = department

    # getter - salary
    def get_salary(self):
        return self.__salary

    # setter - salary
    def set_salary(self, salary):
        self.__salary = salary

    # class method for updating payrise for all employees, working with the class instead of the instance
    @classmethod
    def set_annual_payrise(cls, amount):
        cls.annual_payrise = amount

    # class method to take a standard string of employee data and split it into the right fields
    @classmethod
    def from_string(cls, employee_str):
        first_name, surname, job_title, department, salary = employee_str.split('-')
        return cls(first_name, surname, job_title, department, salary)

    # static method - use these if you don't access the class or in the instance in your function
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
