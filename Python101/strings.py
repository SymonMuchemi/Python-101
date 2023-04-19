course = 'Python\'s course for beginners'
# Characters and their indices
print(course[0])

# Getting the last character in a string of unknown size

print("The last character of the string is", course[-1])
print('The second last character:', course[-2])
print('The third last character:', course[-3])

print('Characters at index 0 to 2:', course[0:3])
print('Characters at to index 4', course[:5])
print('Characters from index 4:', course[4:])

# Cloning a string
another_string = course[:]
print(another_string)

# Formatting strings

first = 'Simon'
last = 'Smith'

message = first, '[' + last + '] is a coder'
formatted_string = f'{first} [{last}] is a coder'
print(formatted_string)

# Length of a string
print(len(formatted_string))

# Changing cases in a string
print(course)
print(course.upper())
print(course.lower())
print(course.title())

# Finding a character or a sequence of characters
print(course.find('P'))
print(course.find('beginners'))
print(course.replace('beginners', 'absolute beginners'))
print(course.replace('o', '0'))

# Boolean expression
print('Python' in course)
print('python' in course)