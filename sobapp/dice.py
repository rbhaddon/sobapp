#!/usr/bin/env python3
'''
    dice and rolling

'''

import random

# Common die sizes for more 'thematic' rolling
D3 = 3
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20
D100 = 100


def roll_die(sides):
    '''
    Roll and individual die with number of sides equal to sides

    If sides is invalid, return 0

    :param int sides:
    :returns: int

    '''
    if sides > 0:
        value = random.randrange(sides) + 1
    else:
        value = 0

    return value


def roll(sides, num=1):
    '''
    Roll multiple dice with the same number of sides

    :param int sides:
    :param int num:
    :returns: int

    '''
    return sum([roll_die(sides) for _ in range(num)])


def roll_d36():
    '''
    Convenience function for rolling D6 * 3 since this is a common action in
    SoB

    '''
    return roll(D6) * 10 + roll(D6)
