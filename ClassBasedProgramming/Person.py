# a simple person class

class Person :
    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age

    def changeAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


person = Person('Brano', 'Bily', 17)
person.changeAge('18')
print person.getAge()
