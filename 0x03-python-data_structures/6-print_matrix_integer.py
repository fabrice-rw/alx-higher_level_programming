#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elm in row:
            if row.index(elm) < len(row) - 1:
                print("{:d}".format(elm), end=' ')
            else:
                print("{:d}".format(elm), end='')
        print("")
