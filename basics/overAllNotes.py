# while loop example
num = 1

while num <= 10:
    print(num)
    num += 1


# for loop
for i in range(1, 11):
  print(i)

# addint something to a list 

bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week


# dictionary are javascript equivalent of objet 
# Dictionary is a collection of key-value pairs. Here’s what it looks like:

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk


dictionary = { "some_key": "some_value" }

for key in dictionary:
    print("%s --> %s" %(key, dictionary[key]))

    dictionary = { "some_key": "some_value" }

for key, value in dictionary.items():
    print("%s --> %s" %(key, value))


# We identify data as attributes and behavior as methods in object-oriented programming. Again:

# Data → Attributes and Behavior → Methods


class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    
    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def set_number_of_wheels(self, number):
        self.number_of_wheels = number


# In Python, we can do that using @property (decorators) to define getters and setters. Let’s see it with code:

# Non-public Instance Variable
# We don’t use the term “private” here, since no attribute is really private in Python (without a generally unnecessary amount of work)

# In Python, we apply a parent class to the child class as a parameter. An ElectricCar class can inherit from our Car class

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

class ElectricCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)

my_electric_car = ElectricCar(4, 5, 250)
print(my_electric_car.number_of_wheels) # => 4
print(my_electric_car.seating_capacity) # => 5
print(my_electric_car.maximum_velocity) # => 250

# Variables declared at class level are not instance variables, they are class attributes. Class attributes are defined outside of all the methods, usually they are placed at the top, right below the class header.

# For example, the pets list in the following code should not be used as a class variable because just a single list would be shared by all Person instances.
class Person:
    # class (shared) attribute
    pets = []
    
    def __init__(self, name, age):       
        # instance (unique) attributes
        self.name = name
        self.age = age


tk = Person('Theo Katz', 38)
ak = Person('Abe Katz', 5)

print(tk.pets, ak.pets)
# [] []

tk.pets.append('dog')
ak.pets.append('cat')

print(tk.pets)
# ['dog', 'cat']     # tk is not supposed to have a 'cat'

print(ak.pets)
# ['dog', 'cat']     # ak is not supposed to have a 'dog'

class Person:
    def __init__(self, name, age):
        # instance (unique) attributes
        self.name = name
        self.age = age
        self.pets = []  


tk = Person('Theo Katz', 38)
ak = Person('Abe Katz', 5)

print(tk.pets, ak.pets)
# [] []

tk.pets.append('dog')
ak.pets.append('cat')

print(tk.pets)
# ['dog']     # tk has a 'dog', as expected

print(ak.pets)
# ['cat']     # ak has a 'cat', as expected