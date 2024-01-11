#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
101-add_attribute.py: Can I?
"""


def add_attribute(self, name, new):
    """function that adds a new attribute to an object if its possible"""
    try:
        self.name = new
    except AttributeError:
        raise TypeError("can't add new attribute")
