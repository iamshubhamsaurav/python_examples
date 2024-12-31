class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
person = Person("Shubham", 22)
print(person.get_name())
print(person.get_age())