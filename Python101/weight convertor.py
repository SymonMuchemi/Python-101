weight = int(input('Enter weight: '))
unit = input('(L)bs or (K)gs: ')

unit = unit.lower()

if unit == 'l':
    weight *= 0.45
    print(f'You are {weight} kilos')
elif unit == 'k':
    weight *= 2.22
    print(f'You are {weight} pounds')
else:
    print('Invalid units')