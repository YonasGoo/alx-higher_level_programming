#!/usr/bin/python3
def add_attribute(obj, attr, value):
    if not hasattr(obj, "__dict__") and not hasattr(type(obj), "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
