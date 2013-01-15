## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## class Dog is an Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has a name
		self.name = name

## Cat is an Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has a name
		self.name = name

## Person is an object
class Person(object)

	def __init__(self, name):
		## Person has a name
		self.name = name

		## Person has a pet of some kind
		self.pet = None

## Employee is a person
class Employee(Person):

	def __init__(self, name, salary):
		##
		super(Employee, self).__init__(name)
		## Employee has a salary
		self.salary = salary

## Fish is an object
class Fish(object):
	pass

## Salmon is a fish
class Salmon(Fish):
	pass

## Halibut is a fish
class Halibut(Fish):
	pass


## rover is a Dog
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has a pet named satan
mary.pet = satan

## Employee Frank has a salary of 120000
frank = Employee("Frank", 120000)

## Frank has a pet named rover
frank.pet = rover

##Flipper is a fish
flipper = Fish()

##course is a Salmon
crouse = Salmon()

##Harry is a halibut
harry = Halibut()
