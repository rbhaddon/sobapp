#!/usr/bin/env python3
'''
    Towns and town generation charts

'''

TOWN_NAMES = {
    1: 'Brimstone',
    2: 'Masthead',
    3: 'Fort Burk',
    4: 'West Witold',
    5: 'Hill Town',
    6: 'Serafin',
    7: 'Fringe',
    8: 'Wood\'s End',
    9: 'Larberg\'s Landing',
    10: 'Stone\'s Crossing',
    11: 'Lestina',
    12: 'Last Chance',
    13: 'Fort Lopez',
    14: 'Adlerville',
    15: 'Flamme\'s Folly',
    16: 'Fort Landy',
    17: 'Conradt\'s Claim',
    18: 'Wilshin\'s Lodge',
    19: 'Seto\'s Mill',
    20: 'San Miguel Mission',
}

TOWN_SIZES = {
    1: 'Small',
    2: 'Small',
    3: 'Small',
    4: 'Small',
    5: 'Medium',
    6: 'Medium',
    7: 'Large',
    8: 'Large',
}

TOWN_KINDS = {
    2: 'Town Ruins',
    3: 'Haunted Town',
    4: 'Plague Town',
    5: 'Rail Town',
    6: 'Standard Frontier Town',
    7: 'Standard Frontier Town',
    8: 'Standard Frontier Town',
    9: 'Mining Town',
    10: 'River Town',
    11: 'Mutant Town',
    12: 'Outlaw Town',
}

TOWN_LOCATIONS = {
    1: 'General Store',
    2: 'Frontier Outpost',
    3: 'Church',
    4: 'Doc\'s Office',
    5: 'Saloon',
    6: 'Blacksmith',
    7: 'Sheriff\'s Office',
    8: 'Gambling Hall',
    9: 'Street Market',
    10: 'Smuggler\'s Den',
    11: 'Mutant Quarter',
    12: 'Indiam Trading Post',
}

def search_dict(value, dct):
    result = None

    if hasattr(value, 'lower'):
        _value = value.lower()
    else:
        _value = value

    for num, name in dct.items():
        if _value in (num, name.lower()):
            result = num
            break

    return result
