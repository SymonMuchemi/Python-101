# name = input('Enter name: ')
# color = input('Enter favourite color: ')
#
# print(name, 'likes', color)

# Convert height to metres
# height = float(input("Enter your height in cm: "))
# print('You are', height / 100, 'metres tall!')

# Comparison operators

name = input("Enter your name: ")

if len(name) < 3:
    print('Name must be at least 3 characters long')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good')