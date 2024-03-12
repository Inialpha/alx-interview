#!/usr/bin/python3
""" a module for the prime game """


def getPrimeNumbers(num):
    """ get the prime numbers """

    allNums = [1] * (num + 1)
    i = 2
    while i <= num:
        if allNums[i] == 1:
            j = i * i
            while j <= num:
                allNums[j] = 0
                j += i
        i += 1

    primes = []
    p = 2
    for p in range(2, num + 1):
        if allNums[p] == 1:
            primes.append(allNums[p])

    return primes


def isWinner(x, nums):
    """ determine the winner of the primegame """
    winners = {'Ben': 0, 'Maria': 0}
    for i in range(x):
        primes = getPrimeNumbers(nums[i])
        if len(primes) % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1
    if winners['Ben'] > winners['Maria']:
        return 'Ben'
    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    else:
        return None
