'''
    Generate fake data for dev testing

    Usage:

    $ python factory.py | json_reformat

'''

from collections import OrderedDict
import json
from random import choice

from faker import Faker


def gen_roll_d36():
    ''' generate ordered output of all 'd36' outcomes '''
    for i in range(1, 7):
        for j in range(1, 7):
            yield i * 10 + j


def gen_roll_d100():
    ''' generate ordered output of all 'd100' outcomes '''
    for i in range(1, 101):
        yield i


def make_town_traits(fake):
    ''' make hexcrawl town traits '''
    chart = OrderedDict()

    for roll in gen_roll_d36():
        data = OrderedDict()
        data['name'] = fake.city()
        data['description'] = fake.catch_phrase()
        chart[roll] = data

    return chart


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

    chart = OrderedDict()

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
        chart[roll] = data

    return chart


def make_encounters(fake):
    ''' make hexcrawl terrain encounters '''
    types = ["Desert Terrain", "Forest Terrain", "Mine Terrain",
             "Mountain Terrain", "Plains Terrain", "Railroad Terrain",
             "River Terrain", "Road Terrain", "Swamp Terrain", "Town Terrain",
             "Town Ruins Terrain", "Growing Dread Encounter"]

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

    chart = OrderedDict()
    for terrain in types:
        terrain_encounters = OrderedDict()
        for roll in range(1, 21):
            encounter = OrderedDict()
            encounter['name'] = fake.company()
            encounter['keywords'] = get_keywords()
            encounter['description'] = fake.paragraph()
            terrain_encounters[roll] = encounter
        chart[terrain] = terrain_encounters

    return chart


def make_madness(fake):
    ''' make hexcrawl madness chart '''
    chart = OrderedDict()
    for roll in gen_roll_d36():
        madness = OrderedDict()
        if roll in (11, 12):
            madness['name'] = 'Brain Dead'
            madness['flavor'] = fake.paragraph()
            madness['effect'] = "Your Hero is Dead"
        else:
            madness['name'] = fake.name()
            madness['flavor'] = fake.paragraph()
            madness['effect'] = fake.sentence()
        chart[roll] = madness

    return chart


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

    chart = OrderedDict()
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
            injury['name'] = name.capitalize()
            injury['flavor'] = fake.paragraph()
            injury['effect'] = fake.sentence()

        chart[roll] = injury

    return chart


def make_mutation(fake):
    ''' make hexcrawl mutation chart '''
    chart = OrderedDict()
    for roll in gen_roll_d36():
        madness = OrderedDict()
        madness['name'] = fake.word()
        madness['effect'] = fake.catch_phrase()
        chart[roll] = madness

    return chart


def factory_main():
    ''' generate all the charts and combine them into one dict '''
    all_data = OrderedDict()
    fake = Faker()

    all_data['town traits'] = make_town_traits(fake)
    all_data['jobs board'] = make_jobs(fake)
    all_data['terrain encounters'] = make_encounters(fake)
    all_data['injury'] = make_injury(fake)
    all_data['madness'] = make_madness(fake)
    all_data['mutation'] = make_mutation(fake)

    return all_data


if __name__ == '__main__':
    print(json.dumps(factory_main()))
