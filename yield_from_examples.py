#! /usr/bin/env python3.3
#-*- coding: utf-8 -*-
"""
Created on Nov 2, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Examples of Python 3.3 yield from statement
"""


# Let's implement our custom version of itertools.chain


def chain2(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


# Let's simplify it


def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        yield from it
