"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
"""
"""
# Operations and functions on a list

numbers = [25, 25, 25, 98, 14, 56, 98]
numbers.append(28)
print(numbers)
numbers.insert(2, 269)
print(numbers)
numbers.remove(56)
print(numbers.count(25))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

number2 = numbers.copy()
numbers.append(2568)
print(number2)
"""
# program to remove duplicates in a list
my_numbers = [25, 1, 2, 2, 3, 88, 88, 9, 9, 25, 14]

for item in my_numbers:
    if my_numbers.count(item) > 1:
        while my_numbers.count(item) > 1:
            my_numbers.remove(item)
my_numbers.sort()
print(my_numbers)

# Option 2

nums = my_numbers.copy()
uniques = []

for number in nums:
    if number not in uniques:
        uniques.append(number)
print(uniques)