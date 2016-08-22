#!/usr/bin/env python3
'''
    Towns and town generation

'''

import charts
import dice

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

class Town:
    max_size = list(TOWN_SIZES.keys())[-1]
    max_jobs = 3

    def __init__(self, name, locations=[], trait=None, kind=None):
        self.name = name
        self._locations = set(locations)
        self._trait = trait
        self._kind, self.kind = None, kind

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{}({}, locations={}, trait={}, kind={})'.format(
            self.__class__.__name__,
            self._name,
            self._locations,
            self._trait,
            self._kind
        )

    @staticmethod
    def roll_size():
        return dice.roll(dice.D8)

    @staticmethod
    def roll_kind():
        return dice.roll(dice.D6, 2)

    @staticmethod
    def roll_trait():
        return dice.roll_d36()

    @staticmethod
    def roll_location():
        return dice.roll(dice.D12)

    @property
    def size(self):
        return TOWN_SIZES.get(len(self._locations), 'Unknown Size')

    @property
    def name(self):
        return TOWN_NAMES.get(self._name, 'Unknown Name')

    @name.setter
    def name(self, value):
        result = search_dict(value, TOWN_NAMES)

        if result is None:
            raise ValueError("Unsupported town name: {}".format(value))
        else:
            self._name = result

    @property
    def kind(self):
        if self._kind is None:
            self._kind = self.roll_kind()

        return TOWN_KINDS.get(self._kind, 'Unsupported Town Kind')

    @kind.setter
    def kind(self, value):
        result = search_dict(value, TOWN_KINDS)

        if result is None:
            raise ValueError("Unsupported town kind: {}".format(value))
        else:
            self._kind = result

    @property
    def trait(self):
        if self._trait is None:
            self._trait = self.roll_trait()

        return charts.TOWN_TRAITS.get(self._trait, 'Unsupported Trait')

    @trait.setter
    def trait(self, value):
        if value in charts.TOWN_TRAITS.keys():
            self._trait = value
        else:
            raise ValueError("Unsupported town trait: {}".format(value))

    @property
    def locations(self):
        if not self._locations:
            self._locations = self.make_locations()

        return [TOWN_LOCATIONS[x] for x in self._locations]

    def make_locations(self):
        size = len(self._locations) or self.roll_size()
        locations = set()
        while len(locations) < size:
            locations.add(self.roll_location())

        return locations

    def is_expandable(self):
        return len(self._locations) < self.max_size

    def create_location(self, num):
        if self.is_expandable():
            if num not in TOWN_LOCATIONS.keys():
                raise ValueError("Unsupported location id: {}".format(num))

            if num in self._locations:
                raise ValueError(
                    "This town already has location id {}".format(num))
            else:
                self._locations.add(num)
