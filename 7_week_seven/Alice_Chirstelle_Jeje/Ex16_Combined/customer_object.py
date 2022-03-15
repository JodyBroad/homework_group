from customer import Customer

Sue = Customer('Sue', 'Smith')

# testing setters
Sue_address = Sue.set_address('2 high street, London, W1 234')
Sue_fullname = Sue.set_full_name('Sue', 'Jonson')

# testing getters
print(Sue.get_full_name())
print(Sue.get_address())
print(Sue.customer_number)
print("Email: " + Sue.get_email())
print(Sue)

# creating a new customer to test auto customer number generator
Amy = Customer('Amy', 'Jackson')
Amy_address = Amy.set_address('10 Downing St, London')
Amy_email = Amy.set_email('Amy@gmail.com')
print(Amy)

