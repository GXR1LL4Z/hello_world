#!/usr/bin/env python

from unicodedata import name


class Dog:
    def __init__(self, name, age):
        #dodajemy tutaj charakterystyczne wartosci obiektu 
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    #.metoda 
    def get_age(self):
        return self.age
    def bark(self):
        print("bark")

d = Dog("Kulus")
d.bark()
d_2 = Dog("Szymon")
print(d.get_name())
print(d_2.name)