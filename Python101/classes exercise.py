class Person:
    def __init__(self, name):
        self.person_name = name

    def talk(self):
        print(f'Hi, I am {self.person_name}.')


Simon = Person('Simon')
Adolph = Person('Hitler')
Adolph.talk()
Simon.talk()