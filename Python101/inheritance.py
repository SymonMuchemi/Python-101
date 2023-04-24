class Mammal:
    def walk(self):
        print('Walk')


class Dog(Mammal):
    def bark(self):
        print('Woof!')


class Cat(Mammal):
    def make_noise(self):
        print('Meow')


dog1 = Dog()
dog1.walk()