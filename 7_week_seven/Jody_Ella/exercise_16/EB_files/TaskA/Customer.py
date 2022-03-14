from Person import Person

class Customer(Person):
    company_name = "CompanyB"
    count = 0

    def __init__(self, name, age, location, spend_amount, number_items_bought):
        super().__init__(name, age, location)
        Customer.count = Customer.count + 1
        self.spend_amount = spend_amount
        self.number_items_bought = number_items_bought

    def items(self, items_bought):
        self.items_bought = list(items_bought)
        print(f'{self.name} has bought {self.items_bought}')

    def shopping(self):
        print(f'{self.name} has spent £{self.spend_amount} at {self.company_name}. They bought {self.number_items_bought} items')