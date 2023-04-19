# Logical AND

has_high_income = 1
has_good_credit = 1
has_criminal_record = 0

if has_high_income and has_good_credit:
    print('Eligible for a loan')

# Logical OR

if has_high_income or has_good_credit:
    print('Eligible for a loan')

# Logical NOT

if has_good_credit and not has_criminal_record:
    print('He is eligible (Criminology Test)')
else:
    print('He\'s not eligible (Criminology test)')