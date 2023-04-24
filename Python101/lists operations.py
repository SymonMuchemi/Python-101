"""
names = ['Simon', 'Mary', 'Leah', 'James', 'David', 'Sarah']
print(names[2::-1])
"""
# Program to write the largest number in a list

myList = [22, 3658, 2567, 5, 525868, 27, 458, 4, 10000, 258, 36]
largest = myList[0]

for item in myList:
    if item > largest:
        largest = item

print(largest)