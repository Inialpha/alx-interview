#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics
"""
from sys import stdin, stdout
try:
    num = 0
    status_dict = {}
    total_size = 0
    for line in stdin:
        num += 1
        line = line.split()
        ip = line[0]
        status = line[-2]
        file_size = line[-1]
        total_size += int(file_size)
        if status in status_dict:
            status_dict[status] += 1
        else:
            status_dict[status] = 1
        if num % 10 == 0:
            print(f"File size: {total_size}")
            for key, value in status_dict.items():
                print(f"{key}: {value}")
except (KeyboardInterrupt, EOFError):
    print(f"File size: {total_size}")
    for key, value in status_dict.items():
        print(f"{key}: {value}")
