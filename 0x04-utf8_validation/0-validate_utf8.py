#!/usr/bin/python3
"""UTF-8 validation module
"""


def check(n):
    """ check if n is a valid following byte """
    print(n)
    return n & 0b11000000 == 0b10000000


def validate(i, data, num_bytes, d_len):
    """ helper function """
    print(data[i])
    # two bytes data
    if d_len - 1 >= num_bytes:
        next_bytes = data[i + 1: i + num_bytes]
        next_bytes = list(map(check, next_bytes))
        if not all(next_bytes):
            return False
    else:
        print("me")
        return False
    return True


def validUTF8(data):
    d_len = len(data)
    skip = 0
    for i in range(d_len):

        if skip > 0:
            skip -= 1
            continue

        if data[i] <= 127:
            continue

        if 191 < data[i] < 224:
            skip = 1
            if not validate(i=i, data=data, num_bytes=2, d_len=d_len):
                return False
        if data[i] & 0b11110000 == 0b11100000:
            skip = 2
            if not validate(i=i, data=data, num_bytes=3, d_len=d_len):
                return False

        if data[i] & 0b11111000 == 0b11110000:
            skip = 3
            if not validate(i=i, data=data, num_bytes=4, d_len=d_len):
                return False

    return True
