case = 1

print("start - to start the car\nstop - to stop te car\nquit - to exit\n")

while case:
    choice = input('>').lower().strip()
    if choice == "start":
        print('Car started...Ready to go')
    elif choice == "stop":
        print('Car stopped')
    elif choice == "quit":
        break
    else:
        print('I don\'t understand')
