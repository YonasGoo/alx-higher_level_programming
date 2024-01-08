#!/usr/bin/python3
def lookup(obj):
    attributes_methods = dir(obj)
    return list(attributes_methods)
