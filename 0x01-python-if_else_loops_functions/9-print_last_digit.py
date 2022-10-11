#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        rem = number % 10
        number = - number
    else:
        rem = number % 10
    print(f"{rem}", end='')
    return rem
