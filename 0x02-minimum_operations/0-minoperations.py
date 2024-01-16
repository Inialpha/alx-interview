#!/usr/bin/python3
""" module to determine minimum operation """

#def copy()
#def paste()
def minOperations(n):
    """ returns the minimum number of operation given n """

    num_op = 0
    num_char = 1
    while n > num_char:
        if n >= num_char * 2:
            clip_board = num_char
            num_op += 1

        num_char += clip_board
        num_op += 1
        
        if n > num_char:
            num_char += clip_board
            num_op += 1

    return num_op
