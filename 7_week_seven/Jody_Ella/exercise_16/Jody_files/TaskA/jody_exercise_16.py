# client script
from person import Person
from employee import Employee
from customer import Customer
import functions
import datetime

# how would we be using this? Possible use cases:
# 1 - create a new customer record when they make first purchase
# 2 - update customer record when they make a subsequent purchase
# 3 - create new employee record when they start
# 4 - update employee record (pay rise, job change etc.)
# should this be two different interfaces? a customer based one and an employee based one?

# instantiating a person, printing their data - wouldn't be using this as this is the superclass and people are either
# employees or customers, not generally just persons
person_1 = Person("Morgana", "Robinson")
functions.print_person_data(person_1)
person_2 = Person("Desiree", "Burch")
functions.print_person_data(person_2)

# instantiating a customer, printing their data
customer_1 = Customer("Mike", "Wozniak", 15, "Email only", ["moustache wax"])
functions.print_customer_data(customer_1)
customer_2 = Customer("Mel", "Giedroyc", 0, "Post and email")
functions.print_customer_data(customer_2)

# adding on a new purchase
customer_1.add_purchase("flip-flops")
# printing total purchase history
functions.print_total_purchase_history(customer_1)
# adding another purchase
customer_1.add_purchase("casserole dish")
# printing total purchase history
functions.print_total_purchase_history(customer_1)
# removing a purchase due to it being returned
customer_1.remove_purchase("flip-flops")
# printing total purchase history
functions.print_total_purchase_history(customer_1)

# adding on loyalty points
customer_1.add_loyalty_points(25)
# printing total loyalty points
functions.print_total_loyalty_points(customer_1)

# checking that these updates stick!
functions.print_customer_data(customer_1)

# instantiating an employee, printing their data
employee_1 = Employee("Nish", "Kumar", "Being comically bad at tasks", "Department of Contestants", 25000)
functions.print_employee_data(employee_1)

# taking in string data with employment info
employee_str_1 = "Alex-Horne-Taskmaster's Assistant-Department of Tasks-0"
employee_str_2 = 'Greg-Davies-Taskmaster-Department of Tasks-100000'
employee_str_3 = 'Tim-Key-Tasks Consultant-Department of Tasks-350'

# using from_string function to split on the hyphens
new_emp_1 = Employee.from_string(employee_str_1)
# printing the data using print_employee_data function
functions.print_employee_data(new_emp_1)

new_emp_2 = Employee.from_string(employee_str_2)
functions.print_employee_data(new_emp_2)

new_emp_3 = Employee.from_string(employee_str_3)
functions.print_employee_data(new_emp_3)

# printing current payrise for the whole class
print("Current annual payrise: ", Employee.annual_payrise)
# printing current payrise for employee_1
functions.print_payrise(employee_1)

# setting payrise for the whole class
Employee.set_annual_payrise(1.07)
# printing new payrise for the whole class
print("New annual payrise: ", Employee.annual_payrise)
# printing new payrise for employee_1

# applying the payrise and printing the new total
functions.print_payrise(employee_1)
functions.print_payrise(new_emp_2)

my_date = datetime.date(2022, 3, 14)
print(f'Is {my_date} a workday? {Employee.is_workday(my_date)}')

# an easy way to look at inheritance etc. for classes
# print(help(Employee))
