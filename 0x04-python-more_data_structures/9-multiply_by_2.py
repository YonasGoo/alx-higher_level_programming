#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiDict = {}
    for key, value in a_dictionary.items():
        multiDict[key] = value * 2
    return multiDict
