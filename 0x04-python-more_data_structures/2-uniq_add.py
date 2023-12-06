#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqSet = set()
    for num in my_list:
        uniqSet.add(num)
    return sum(uniqSet)
