#! /usr/bin/env python3.4
#-*- coding: utf-8 -*-
"""
Created on Nov 2, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Examples of the new Python 3.4  single dispatch mechanism
"""


# Let's define some animals

class Duck:
    def quack(self):
        print("quack")


class Cat:
    def meow(self):
        print("meow")


class Dog:
    def bark(self):
        print("bark")


class Cow:
    def moo(self):
        print("moo")


donald = Duck()
garfield = Cat()
milu = Dog()
milka = Cow()


# Function to play animals sounds


def make_sound(animal):
    if isinstance(animal, Duck):
        animal.quack()
    elif isinstance(animal, Cat):
        animal.meow()
    elif isinstance(animal, Dog):
        animal.bark()
    else:
        raise NotImplementedError("Unknown animal")

make_sound(donald)
make_sound(garfield)
make_sound(milu)
make_sound(milka)


# Let's simplify this implementation


import functools


@functools.singledispatch
def make_sound(animal):
    raise NotImplementedError("Unknown animal")


@make_sound.register(Duck)
def make_duck_sound(animal):
    animal.quack()


@make_sound.register(Cat)
def make_cat_sound(animal):
    animal.meow()


@make_sound.register(Dog)
def _(animal):
    animal.bark()


make_sound(donald)
make_sound(garfield)
make_sound(milu)
make_sound(milka)
