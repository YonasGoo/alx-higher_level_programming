#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
7-base_geometry.py: Geometry module
"""


class BaseGeometry:
    """create a class"""
    pass

    def area(self):
        """public instance method for calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method  that validates value"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
