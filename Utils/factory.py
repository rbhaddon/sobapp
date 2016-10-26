#!/usr/bin/env python3
'''
    Generate fake data for dev testing

    Usage:

    $ python factory.py | json_reformat

'''

from collections import OrderedDict
from functools import wraps
import json
from random import choice
import os.path

from faker import Faker

OUTDIR = "../Assets/StreamingAssets"
OUTDIR = "/tmp"

def gen_roll_d36():
    ''' generate ordered output of all 'd36' outcomes '''
    for i in range(1, 7):
        for j in range(1, 7):
            yield i * 10 + j


def gen_roll_d100():
    ''' generate ordered output of all 'd100' outcomes '''
    for i in range(1, 101):
        yield i


def hc_chart(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        chart = []
        for roll, data in func(*args, **kwargs):
            entry = OrderedDict()
            entry['roll'] = roll
            entry['data'] = data
            chart.append(entry)

        return chart
    return wrapper


@hc_chart
def make_town_traits(fake):
    ''' make hexcrawl town traits '''

    for roll in gen_roll_d36():
        data = OrderedDict()
        data['name'] = fake.city()
        data['description'] = fake.catch_phrase()

        yield (roll, data)


@hc_chart
def make_jobs(fake):
    ''' make hexcrawl jobs '''
    locations = [
        'Random Town',
        'Random Mine',
        'Random Hex',
        'Local Town',
    ]

    keywords = [fake.city() for _ in range(100)]
    keywords = [
        'Fight',
        'Supernatural',
        'Delivery',
        'Rumor',
        'Investigate',
        'Train',
        'Undead',
        'Frontier',
        'Murder',
        'Find',
        'Settler',
        'Bounty',
        'Strange',
        'Labor',
        'Politics',
        'Occult',
        'Youth',
        'Research',
        'Holy',
        'Law',
        'Outlaw',
        'Performer',
        'Traveler',
        'Tribal',
        'Negotiation',
        'Personal',
        'Mine',
        'Merchant',
        'Science',
        'Escort',
        'Mandatory!',
        'Mandatory!',
        'Mandatory!',
        'Mandatory!',
    ]

    def get_keywords():
        ''' make a semi random list with no repeated terms '''
        kw_set = set()
        while len(kw_set) < 2:
            kw_set.add(choice(keywords))

        # ensures 'Job' is first
        return ['Job'] + list(kw_set)

    for roll in gen_roll_d100():
        data = OrderedDict()
        data['title'] = fake.job()
        data['keywords'] = get_keywords()
        data['background'] = fake.sentence()
        data['location'] = choice(locations)
        data['time'] = choice([0, 0, 5, 7, 10, 15])
        data['description'] = fake.paragraphs()
        data['reward'] = fake.paragraph()
        data['failure'] = fake.paragraph()

        yield (roll, data)


@hc_chart
def make_encounters(fake):
    ''' make hexcrawl terrain encounters '''
    keywords = [
        "Active",
        "Active",
        "Active",
        "Active",
        "Active",
        "Active",
        "Tribal",
        "Scavenge",
        "Water",
        "Environmental",
        "Explore",
        "Weather",
        "Creature",
        "Merchant",
        "Horror",
        "Void",
        "Mission",
        "Monster",
        "Supernatural",
        "Stranger",
        "Loot",
        "Swarm",
        "Fire",
        "Enemy",
        "Hazard",
        "Pit",
        "Disease",
        "Hope",
        "Gambling",
        "Outlaw",
        "Transport",
        "Dark Stone",
        "Lost",
        "Charm",
        "Poison",
        "Madness",
        "Cult",
        "Ghost",
        "Undead",
        "Darkness",
    ]

    def get_keywords():
        ''' make a semi random list with no repeated terms '''
        kw_set = set()
        while len(kw_set) < 2:
            kw_set.add(choice(keywords))

        # ensures 'Enounter' is first
        return ['Encounter'] + list(kw_set)

    for roll in range(1, 21):
        encounter = OrderedDict()
        encounter['name'] = fake.company()
        encounter['keywords'] = get_keywords()
        encounter['description'] = fake.paragraph()

        yield (roll, encounter)


@hc_chart
def make_madness(fake):
    ''' make hexcrawl madness chart '''
    for roll in gen_roll_d36():
        madness = OrderedDict()
        if roll in (11, 12):
            madness['name'] = "Brain Dead"
            madness['flavor'] = "You are nothing but an empty shell now."
            madness['effect'] = "Your Hero is Dead"
        else:
            madness['name'] = fake.word().capitalize()
            madness['flavor'] = fake.paragraph()
            madness['effect'] = fake.sentence()

        yield (roll, madness)


@hc_chart
def make_injury(fake):
    ''' make hexcrawl injury chart '''
    body_parts = [
        "brain",
        "knee",
        "leg",
        "foot",
        "hand",
        "neck",
        "back",
        "genitals",
        "eye",
        "ear",
        "elbow",
        "spleen",
        "kidney",
        "heart",
        "stomach",
        "rectum",
        "face",
        "teeth",
        "nose"
    ]
    maladies = [
        "crushed",
        "bruised",
        "scratched",
        "torn",
        "lacerated",
        "broken",
        "bleeding",
        "fractured",
        "butchered",
        "twisted",
        "pulled",
        "dislocated"
    ]

    used_names = []
    for roll in gen_roll_d36():
        injury = OrderedDict()
        if roll in (11, 12):
            injury['name'] = 'Eviscerated'
            injury['flavor'] = ('You have seconds left to say any famous last '
                                'words before you fall to the  oor and die.')
            injury['effect'] = 'Your Hero is Dead'
        else:
            name = '{} {}'.format(choice(maladies), choice(body_parts))
            while name in used_names:
                name = '{} {}'.format(choice(maladies), choice(body_parts))
            used_names.append(name)
            injury = OrderedDict()
            injury['name'] = name.title()
            injury['flavor'] = fake.paragraph()
            injury['effect'] = fake.sentence()

        yield (roll, injury)


@hc_chart
def make_mutation(fake):
    ''' make hexcrawl mutation chart '''
    for roll in gen_roll_d36():
        mutation = OrderedDict()
        mutation['name'] = fake.word().capitalize()
        mutation['effect'] = fake.catch_phrase()

        yield (roll, mutation)



def factory_main():
    ''' generate all the charts and combine them into one dict '''
    fake = Faker()
    chart_tuples = [
        ('town_traits', make_town_traits),
        ('jobs_board', make_jobs),
        ('injuries', make_injury),
        ('madnesses', make_madness),
        ('mutations', make_mutation),
    ]

    enc_types = ["Desert Terrain", "Forest Terrain", "Mine Terrain",
             "Mountain Terrain", "Plains Terrain", "Railroad Terrain",
             "River Terrain", "Road Terrain", "Swamp Terrain", "Town Terrain",
             "Town Ruins Terrain", "Growing Dread Encounter"]

    terrains = ["desert", "forest", "mine", "mountain", "plains", "railroad",
             "river", "road", "swamp", "town", "townruins", "growingdread"]
    
    for terrain in terrains:
        chart_tuples.append(
            ('terrain_encounter_{}'.format(terrain), make_encounters)
        )

    prefix = 'hc_'
    for chart_name, func in chart_tuples:
        filename = os.path.join(
            OUTDIR,
            '{p}{n}.json'.format(p=prefix, n=chart_name)
        )
        with open(filename, 'w') as out:
            print('\tWriting {}'.format(filename))
            json.dump({"array": func(fake)}, out, indent=4)

if __name__ == '__main__':
    print("Warning: This will overwrite previously generated HC charts!")
    try:
        input("Continue?")
    except KeyboardInterrupt:
        print("Canceled.")
    else:
        factory_main()
