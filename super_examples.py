#! /usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Created on Nov 2, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Examples of Python 3.0 super function
"""


# Let's subclass Python's dict


class SilentDict(dict):
    def __getitem__(self, key):
        """Called to implement evaluation of self[key]
        :returns: None by default
        """
        try:
            return super(SilentDict, self).__getitem__(key)
        except KeyError:
            return None


d = SilentDict({"a": 1, "b": 2})
print(d["a"])
print(d["c"])


# Let's simplify it


class SilentDict(dict):
    def __getitem__(self, key):
        """Called to implement evaluation of self[key]
        :returns: None by default
        """
        try:
            return super().__getitem__(key)
        except KeyError:
            return None


d = SilentDict({"a": 1, "b": 2})
print(d["a"])
print(d["c"])
