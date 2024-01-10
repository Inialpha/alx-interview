#!/usr/bin/python3
""" module contain canUnlockAll(boxes) function """


def canUnlockAll(boxes):
    """ function determines if all boxes can opened """
    myKeys = boxes[0]
    opened = [0]
    openedboxes = [boxes[0]]

    for mykey in myKeys:
        if mykey not in opened and mykey < len(boxes):
            myKeys.extend(boxes[mykey])
            opened.append(mykey)
            openedboxes.append(boxes[mykey])

    return len(openedboxes) == len(boxes)
