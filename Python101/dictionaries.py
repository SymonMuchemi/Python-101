# Dictionaries are used to store key-value pairs
# Keys should be unique

customer = {
    "name": 'John Doe',
    'age': 22,
    'is_verified': True
}

# Accessing values
print(customer.get('is_verified'))

# Updating values
customer['name'] = 'Jack Smith'
print(customer['name'])

# Adding a new key-value pair
customer['height'] = '175 Cm'
print(customer)

