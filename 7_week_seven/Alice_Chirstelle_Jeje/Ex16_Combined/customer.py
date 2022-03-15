from person import Person


class Customer(Person):
    customer_number = 0

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Inheritance
        Customer.customer_number += 1

    # def set_customer_number(self, customer_number):
    #     self.customer_number = customer_number

    def get_customer_number(self):
        return self.customer_number

    def __str__(self):
        customer_info = "Customer number: " + str(self.get_customer_number()) + "\n"
        customer_info += "Full name: " + self.get_full_name() + "\n"
        customer_info += "Address: " + self.get_address() + "\n"
        customer_info += "Email: " + self.get_email() + "\n"
        return customer_info



