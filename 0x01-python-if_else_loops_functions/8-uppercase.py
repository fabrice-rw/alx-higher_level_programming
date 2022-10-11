#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            a = ord(c) - 32
        else:
            a = ord(c)
        print("{}".format(chr(a)), end='')
    print("")
