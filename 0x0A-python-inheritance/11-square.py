#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def init(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.width * self.height

    def str(self):
        return f"[Rectangle] {self.width}/{self.height}"

    def print(self):
        print(self.str())

class Square(Rectangle):
    def init(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().init(size, size)

    def str(self):
        return f"[Square] {self.size}/{self.size}"

    def print(self):
        print(self.str())
