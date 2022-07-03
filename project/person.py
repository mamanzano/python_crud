from unicodedata import name


class Person:

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def say_my_name(self):
        print('My name is {} and i am {} years old'.format(self.name,self.age))


if __name__ == '__main__':
    person = Person('Mario Manzano',36)
    print('Age: {}'.format(person.age))
    person.say_my_name() 