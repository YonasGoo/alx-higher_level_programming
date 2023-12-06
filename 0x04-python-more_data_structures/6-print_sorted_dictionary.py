#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedKeys = sorted(a_dictionary.keys())
    for key in sortedKeys:
        print(f"{key}: {a_dictionary[key]}")
