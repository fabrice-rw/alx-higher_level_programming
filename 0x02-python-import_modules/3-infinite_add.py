#!/usr/bin/python3

from sys import argv
i = 1
add = 0
if __name__ == "__main__":
    while i < len(argv):
        add += int(argv[i])
        i += 1
    print(add)
