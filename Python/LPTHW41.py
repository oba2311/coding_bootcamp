# animal is=a pbject
class Animal(object):
    pass

# Dog is an object
class Dog(Animal):

# Dog has a name:
    def __init__(self, name):
        self.name = name

# Cat is an object:
class Cat(Animal):

# cat has a name
    def __init__(self, name):
        self.name = name

# person is an object:
class Person(object):

# person has a name and a pet, sometimes:
    def __init__(self, name):
        self.name = name
        self.pet = None

# Employee is an object:
class Employee  (Person):
# what's this?
# Employee has a name? and a salary
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

# fish is an object
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# rover is a Dog object  with the name Rover:
rover = Dog("Rover")
# same:
satan = Cat("Satan")
# same:
mary = Person("Mary")
# mary has a pet that is a cat by the name satan:
mary.pet = satan
# frank is an Employee by the name frank who makes 120000:
frank = Employee("Frank", 120000)
# frank also has a pet which is a dog by the name rover:
frank.pet = rover
# flipper is a fish:
flipper = Fish()
crouse = Salmon()
harry = Halibut()
