#!/usr/bin/python3
""" module to determine minimum operation """


def minOperations(n):
    """ returns the minimum number of operation given n """

    if not isinstance(n, int):
        return 0
    divisor = 2
    num_op = 0
    while n >= divisor:
        if n % divisor == 0:
            num_op += divisor
            n /= divisor
        else:
            divisor += 1

    return num_op
