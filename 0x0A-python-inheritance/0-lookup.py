#!/usr/bin/python3
"""Defines a function that returns attributes and methods of an object"""


def lookup(obj):
    attributes_methods = dir(obj)
    return list(attributes_methods)
