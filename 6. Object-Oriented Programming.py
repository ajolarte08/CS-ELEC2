class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name + "'s age is " + str(self.age))

Lenor = Person("Lenor", 42)
Lenor.show()