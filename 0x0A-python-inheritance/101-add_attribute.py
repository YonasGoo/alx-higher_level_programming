#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    if hasattr(obj, "dict") or (hasattr(type(obj), "slots") and attribute in type(obj).slots):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
