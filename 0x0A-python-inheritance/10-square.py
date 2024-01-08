#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise NotImplementedError("Subclass must implement area method.")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


class Square(Rectangle):
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
