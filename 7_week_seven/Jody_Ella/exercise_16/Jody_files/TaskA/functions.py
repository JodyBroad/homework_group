from person import Person
from employee import Employee
from customer import Customer


def print_person_data(person_number):
    # print('Person name:', person_number.get_person_name())
    print('Person full name:', person_number.fullname())

    print("Person records created: ", Person.num_created)


def print_customer_data(customer_number):
    print('Customer name: ', customer_number.get_person_name())
    print('Customer purchase history: ', customer_number.get_purchase_history())
    print('Customer loyalty points: ', customer_number.get_loyalty_points())
    print('Customer marketing preferences: ', customer_number.get_marketing())

    print("Customer records created: ", Customer.num_of_customers)


def print_customer_name(customer_number):
    print('Customer name: ', customer_number.get_person_name())


def print_total_loyalty_points(customer_number):
    print('New customer loyalty points total for', Person.fullname(customer_number), ':',
          customer_number.total_loyalty_points())


def print_total_purchase_history(customer_number):
    print('New customer purchase history for', Person.fullname(customer_number), ':',
          customer_number.total_purchase_history())


def print_employee_data(employee_number):
    print('Employee name:', employee_number.get_person_name())
    print('Employee Department: ', employee_number.get_department())
    print('Employee job title: ', employee_number.get_job_title())
    print('Employee salary: ', employee_number.get_salary())

    print("Employee records created: ", Employee.num_of_employees)


def print_payrise(employee_number):
    print(f'{employee_number.get_person_name()} - your pay next year is: £{employee_number.apply_payrise():.2f}')
