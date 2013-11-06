#! /usr/bin/env python3.4
#-*- coding: utf-8 -*-
"""
Created on Nov 2, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Examples of the Python 3.3  raise from None statement
"""

from urllib.request import urlopen
from urllib.error import URLError


class CustomException(Exception):
    """Out custom exception for this example"""


def requester(url):
    """Open and read given url"""
    try:
        return urlopen(url).readall()
    except URLError as exc:
        raise CustomException from exc


def call_the_requester(url):
    return requester(url)


def main_app(url):
    print(call_the_requester(url))


if __name__ == "__main__":
    main_app("http://unknown_host:8765")
