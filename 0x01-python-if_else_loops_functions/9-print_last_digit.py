#!/usr/bin/python3
def print_last_digit(number):
    a = 1
    if (number < 0):
        a = -1
        lastDigit = (number * a) % 10
        print("{:d}".format(lastDigit), end='')
        return (lastDigit)
