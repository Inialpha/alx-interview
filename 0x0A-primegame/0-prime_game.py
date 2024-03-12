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

    return allNums


def isWinner(x, nums):
    """ determine the winner of the primegame """
    winners = {'Ben': 0, 'Maria': 0}
    for num in nums:
        primes = getPrimeNumbers(num)
        if len(primes[2:]) % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1
    if winners['Ben'] > winners['Maria']:
        return 'Ben'
    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    else:
        return None
