from person import Person


class Employee(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.__base_salary = 0
        self.__job_title = " "
        self.__fte = 0
        self.__actual_salary = 0
        self.__raise_amount = 0
        self.__raise_applied = 0

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_job_title(self):
        return self.__job_title

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def get_base_salary(self):
        return self.__base_salary

    def set_fte(self, fte):
        self.__fte = fte

    def get_fte(self):
        return float(self.__fte)

    def calculate_actual_salary(self):
        actual_salary = self.get_base_salary() * self.get_fte()
        return actual_salary

    def apply_raise(self, raise_percentage):
        # Alice updated this so that when the get_base_salary function is called after a raise has been applied,
        # the new 'raise applied' salary value is returned

        # self.__raise_amount = raise_amount
        raise_applied = self.get_base_salary() * (1 + raise_percentage)
        self.__base_salary = 0
        self.__base_salary += raise_applied
        return raise_applied

    def __str__(self):
        employee_info = super().__str__() + "\n"
        employee_info += "Job title: " + self.get_job_title() + "\n"
        employee_info += "Base salary: " + str(self.get_base_salary()) + "\n"
        employee_info += "FTE: " + str(self.get_fte()) + "\n"
        employee_info += "Actual salary: " + str(self.calculate_actual_salary()) + "\n"
        return employee_info
