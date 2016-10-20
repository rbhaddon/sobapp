#!/usr/bin/env python3
'''
    Towns and town generation

'''

import enum
from random import choice

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


class World:
    '''

    '''
    def __init__(self, name):
        self.name = name
        self.initialized = False
        self._img_hi = None
        self._img_lo = None
        self.towns = {}

    def generate(self):
        jobs_available = list(charts.JOBS_BOARD.keys())
        for num in range(1, len(TOWN_NAMES) + 1):
            town = Town(num)
            if num in (1,):
                town.destroy()
            else:
                town.initialize()
                jobs = []
                for _ in range(Town.max_jobs):
                    job_num = choice(jobs_available)
                    jobs_available.remove(job_num)
                    jobs.append(Job(job_num))
                town.jobs = jobs

            self.towns[num] = town


class JobStatus(enum.Enum):
    unclaimed = 'Unclaimed'
    claimed = 'Claimed'
    completed = 'Completed'
    failed = 'Failed'


class Job:
    def __init__(self, num):
        # pylint: disable=unsubscriptable-object
        self.data = charts.JOBS_BOARD[num]
        self._status = JobStatus.unclaimed
        self._origin = None
        self._days = 0

    @property
    def status(self):
        return self._status.value

    @status.setter
    def status(self, value):
        if isinstance(JobStatus, value):
            self._status = value
        else:
            try:
                # pylint: disable=unsubscriptable-object
                self._status = JobStatus[value.lower()]
            except (KeyError, AttributeError):
                raise KeyError('Attempted to set invalid Job status')

    @property
    def time_remaining(self):
        return 0

    @property
    def mandatory(self):
        return 'Mandatory!' in self.data['keywords']

    @property
    def title(self):
        return self.data['title']

    @property
    def keywords(self):
        return ', '.join(self.data['keywords'])

    @property
    def background(self):
        return self.data['background']

    @property
    def location(self):
        return self.data['location']

    @property
    def time(self):
        return self.data['time']

    @property
    def description(self):
        return self.data['description']

    @property
    def reward(self):
        return self.data['reward']

    @property
    def failure(self):
        return self.data['failure']


class Town:
    max_size = list(TOWN_SIZES.keys())[-1]
    max_jobs = 3

    def __init__(self, name, locations=[], trait=None, kind=None, jobs=[]):
        self.destroyed = False
        self.name = name
        self._locations = locations
        self._trait = trait
        self._kind = kind
        self._jobs = jobs

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

    def destroy(self):
        self._locations = []
        self._jobs = []
        self._trait = None
        self.destroyed = True

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
            kind = str(self._kind)
        else:
            kind = TOWN_KINDS.get(self._kind, 'Unsupported Town Kind')

        return kind

    @kind.setter
    def kind(self, value):
        if not self.destroyed:
            result = search_dict(value, TOWN_KINDS)

            if result is None:
                raise ValueError("Unsupported town kind: {}".format(value))
            else:
                self._kind = result

    @property
    def trait(self):
        if self._trait is None:
            trait = str(self._trait)
        else:
            trait = charts.TOWN_TRAITS.get(self._trait, 'Unsupported Trait')

        return trait

    @trait.setter
    def trait(self, value):
        if not self.destroyed:
            if value in charts.TOWN_TRAITS.keys():
                self._trait = value
            else:
                raise ValueError("Unsupported town trait: {}".format(value))

    @property
    def jobs(self):
        return self._jobs

    @jobs.setter
    def jobs(self, joblist):
        self._jobs = joblist

    @property
    def locations(self):
        return [TOWN_LOCATIONS[x] for x in self._locations]

    def make_locations(self, size):
        locations = set()
        while len(locations) < size:
            locations.add(self.roll_location())

        return list(locations)

    def is_expandable(self):
        if self.destroyed:
            return False
        else:
            return len(self._locations) < self.max_size

    def add_location(self, num):
        if self.is_expandable():
            if num not in TOWN_LOCATIONS.keys():
                raise ValueError("Unsupported location id: {}".format(num))

            if num in self._locations:
                raise ValueError(
                    "This town already has location id {}".format(num))
            else:
                self._locations.append(num)

    def del_location(self, num):
        try:
            self._locations.remove(num)
        except ValueError:
            pass

        return TOWN_LOCATIONS.get(num)

    def initialize(self):
        '''


        '''
        self._locations = self.make_locations(self.roll_size())
        self._trait = self.roll_trait()
        self._kind = self.roll_kind()
        self.destroyed = False
