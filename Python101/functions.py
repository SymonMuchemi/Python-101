def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name}\nWelcome aboard')


def square(number):
    return number * number


print(square(20))
print('Start')
greet_user('Simon', 'Cowell')

# Key word arguments
# Add readability to the code especially when using numerical data
# Positional argument should begin then positional arguments
greet_user(last_name='Muchemi', first_name='Simon')
print('Finish')
