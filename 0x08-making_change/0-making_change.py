#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):

    if total <= 0:
        return 0
    total_num = 0
    change = 0
    while change != total:
        bal = total
        new_coin = 0
        for coin in coins:
            if total - (change + coin) < bal and change + coin <= total:
                bal = total - (change + coin)
                new_coin = coin
        if new_coin == 0:
            return -1
        change += new_coin
        total_num += 1

    return total_num
