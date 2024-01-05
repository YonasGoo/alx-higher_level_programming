#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        else:
            self.__dict__[name] = value
