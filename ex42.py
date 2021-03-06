# # Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# # Class Dog is-a(n) Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Class Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
    
    def meow():
        print("Everyday is caturday.")

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary 
        self.salary = salary

## Fish is-a object
class Fish(object):
    
    def __init__(self, name):
        self.name = name

    def fishface(self):
        print("Every face is a fishface.")

    def fish_list(self):
        print(f"I have things to say: {self.name}")

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut us-a Fish
class Halibut(Fish):
    pass


## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Satan is-a Pet
mary.pet = satan

## Employee has-a frank
frank = Employee("Frank", 120000)

## frank has-a rover
frank.pet = rover

## flipper is a Fish
flipper = Fish("Flipper")

## crouse is-a Salmon
crouse = Salmon("Totally not a fish.")

## harry is-a Halibut
harry = Halibut("I'm sorry, I did it for the halibut.")

flipper.fishface()
flipper.fish_list()
crouse.fish_list()
