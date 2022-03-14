# customer is subclass of person, so need to import
from person import Person


class Customer(Person):
    num_of_customers = 0

    def __init__(self, first_name, surname, loyalty_points, marketing, purchase_history=None):
        super().__init__(first_name, surname)
        if purchase_history is None:
            self.__purchase_history = []
        else:
            self.__purchase_history = purchase_history
        self.__loyalty_points = loyalty_points
        self.__marketing = marketing
        Customer.num_of_customers += 1

    # getter - purchase history
    def get_purchase_history(self):
        return self.__purchase_history

    # setter - purchase history
    def set_purchase_history(self, purchase_history):
        self.__purchase_history = purchase_history

    # getter - loyalty points
    def get_loyalty_points(self):
        return self.__loyalty_points

    # setter - loyalty points
    def set_loyalty_points(self, loyalty_points):
        self.__loyalty_points = loyalty_points

    def add_loyalty_points(self, add_loyalty_points):
        self.__loyalty_points += add_loyalty_points
        return

    def total_loyalty_points(self):
        return self.__loyalty_points

    def add_purchase(self, add_purchase):
        if add_purchase not in self.__purchase_history:
            self.__purchase_history.append(add_purchase)
        return

    def remove_purchase(self, remove_purchase):
        if remove_purchase in self.__purchase_history:
            self.__purchase_history.remove(remove_purchase)
        return

    def total_purchase_history(self):
        return self.__purchase_history

    # getter - marketing
    def get_marketing(self):
        return self.__marketing

    # setter - marketing
    def set_marketing(self, marketing):
        self.__marketing = marketing
