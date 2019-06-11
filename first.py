import os 
import sys
import random



def fibonacci(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonacci(20000)

class Animal:
    _name = ''
    _weight = 0
    _sound = ''
    _height = 0

    def __init__(self, name, weight, sound, height):
        self._name = name
        self._weight = weight
        self._sound = sound
        self._height = height

    def setName(self, name):
        self._name = name

    def getName(self, name):
        return self._name
    
    def getType(self):
        print("Animal")

    def toString(self):
        return "{} is {} tall and weights {} and says {}".format(self._name, self._height, self._weight, self._sound)

cat = Animal("Wiskers", 10, "miow", 33)
print(cat.toString())

class Dog(Animal):
    _owner = ''

    def __init__(self, name, weight, sound, height, owner):
        self._owner = owner
        super(Dog, self).__init__(name, weight, sound, height)

    def getType(self):
        print("Dog")
    
    def toString(self):
        return "{} is {} tall and weights {} and says {}. His owner is {}".format(self._name,
                self._height, self._weight, self._sound, self._owner)


dogi = Dog("Felek", 22, "bark", 44, "norbert")
print(dogi.toString())

class TestAnimal:
    def getType(self, animal):
        animal.getType()
# polymorphism, automatically knows which getType should be invoked
test = TestAnimal()
test.getType(cat)
test.getType(dogi)