from Customer import Customer
from Employee import Employee
from Person import Person

jade = Person("Jade", 36, "London")
jade.show()


# Employee Class
james = Employee("James", 23, "London", "Finance", 33000, 5367789)
sarah = Employee("Sarah", 29, "Manchester", "Marketing", 55000, 54345567)

print(f'The total number of employees at {Employee.company_name} is {Employee.count}')

james.work()
sarah.work()


# Customer Class
jasmine = Customer("Jasmine", 35, "Sheffield", 53, 4)

print(f'{Customer.company_name} has had {Customer.count} customers')

jasmine.show()
jasmine.shopping()
jasmine.set_age(36)
jasmine.show()
jasmine.items(["Shampoo", "bananas"])