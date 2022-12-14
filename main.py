
# write your code here

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'You are {self.name} and you are {self.age} years old.'
    def is_adult(self):
        if self.age > 18:
            print('You have too much responsibilties')
        else :
            print('You are Lucky')

first_person = Person('Aziz', 24)

print(first_person.is_adult())
print(first_person)