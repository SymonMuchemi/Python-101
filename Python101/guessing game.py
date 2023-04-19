secret = 9
guesses = 0

while guesses < 3:
    guesses += 1
    number = int(input('Guess: '))
    if number != secret:
        print('You got it wrong')
    else:
        print('Correct!')
        break
else:
    print(f'You failed\nThe number was {secret}')
