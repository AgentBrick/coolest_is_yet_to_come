#! /usr/bin/env python3.4
#-*- coding: utf-8 -*-
"""
Created on Nov 2, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Examples of the new Python 3.4  Enum module
"""


# Let’s implement a traffic light


RED, ORANGE, GREEN = range(3)  # Colors
STOPPED, RUNNING = range(2)    # Statuses


class TrafficLightO:
    def __init__(self, light_color, status):
        assert light_color in (RED, ORANGE, GREEN), "Not a valid color"
        assert status in (RUNNING, STOPPED), "Not a valid status"
        self.color = light_color
        self.status = status
    def print_state(self):
        color_name = "red" if self.color == RED else "green" if self.color == GREEN else "orange"
        status_name = "running" if self.status == RUNNING else "stopped"
        print("Traffic light is {} in color {}".format(status_name, color_name))


my_semaphore = TrafficLight(RUNNING, RED)
my_semaphore.print_state()


# Let me introduce the enum module


from enum import Enum


Color = Enum("Color", "red orange green")   # Colors
Status = Enum("Status", "stopped running")  # Statuses


class TrafficLight:
    def __init__(self, light_color, status):
        assert light_color in Color, "Not a valid color"
        assert status in Status, "Not a valid status"
        self.color = light_color
        self.status = status

    def print_state(self):
        color_name = "red" if self.color == Color.red else "green" if self.color == Color.green else "orange"
        status_name = "running" if self.status == Status.running else "stopped"
        print("Traffic light is {} in color {}".format(status_name, color_name))


my_semaphore = TrafficLight(Status.running, Color.red)

my_semaphore = TrafficLight(Color.red, Status.running)
my_semaphore.print_state()


STOPPED is RED and RUNNING is ORANGE
(RUNNING + ORANGE) * GREEN


# More enum examples


class Color(Enum):  # enumaration
    red = 0
    orange = 10  # enumeration members
    green = 20   # custom non-consecutive values
    ruby = 0     # aliases

print(Color.green)
print(repr(Color.green))

print(repr(Color.ruby))    # this is an alias

print(Color.orange.name)   # we can retrieve a member name
print(Color["orange"])     # we can get the enum member from its name

print(Color.orange.value)  # we can retrieve a member value
print(Color(1))            # we can get the enum member from its value


class Color(Enum):
    red = 0
    orange = 10
    green = 20

class Status(Enum):
    running = 0
    stopped = 1

class TrafficLight:
    def __init__(self, light_color, status):
        assert light_color in Color, "Not a valid color"
        assert status in Status, "Not a valid status"
        self.color = light_color
        self.status = status

    def print_state(self):
        print("Traffic light is {} in color {}".format(self.status.name, self.color.name))

my_semaphore = TrafficLight(Color.red, Status.running)
my_semaphore.print_state()
