#!/usr/bin/env python3
'''
    Charts for HexCrawl

'''

from collections import namedtuple

TownTrait = namedtuple('TownTrait', ['name', 'description'])

TOWN_TRAITS = {
    11: TownTrait("Dry", "This Town has declared alcohol to be a vile sin and forbids the purchase of or the imbibing of any alcoholic demon drink. Heroes may not purchase any alcoholic Side Bag Tokens here but may attempt to sell them at the Camp Site for twice the price. When attempting to sell, roll a D6. On a 1 or 2, the sale is discovered and the Heroes must end their Town Stay and cannot enter Town for a week."),
    12: TownTrait("Dark Secret", ""),
    13: TownTrait("No Stones Allowed!", ""),
    14: TownTrait("Dark Stone Infused", ""),
    15: TownTrait("Shortages", ""),
    16: TownTrait("Obligation", ""),
    21: TownTrait("Degenerate", ""),
    22: TownTrait("Bad Water", ""),
    23: TownTrait("Inbred", ""),
    24: TownTrait("Xenophobic", ""),
    25: TownTrait("Unstable Gate", ""),
    26: TownTrait("Foreigners", ""),
    31: TownTrait("Heathens", ""),
    32: TownTrait("Cannibals!", ""),
    33: TownTrait("Religious Cult", ""),
    34: TownTrait("Boring", ""),
    35: TownTrait("Bartering", ""),
    36: TownTrait("Corrupt", ""),
    41: TownTrait("Thieving", ""),
    42: TownTrait("Slavers", ""),
    43: TownTrait("Amazonian", ""),
    44: TownTrait("Peaceful", ""),
    45: TownTrait("Addicted", ""),
    46: TownTrait("Nightmares", ""),
    51: TownTrait("Artifact Decay", ""),
    52: TownTrait("Bad Luck", ""),
    53: TownTrait("Black Market", ""),
    54: TownTrait("Jovial", ""),
    55: TownTrait("Constructive", ""),
    56: TownTrait("Cattle Yard", ""),
    61: TownTrait("Law Abiding", ""),
    62: TownTrait("Fancy House", ""),
    63: TownTrait("Unstable Economy", ""),
    64: TownTrait("Dimensional Paradox", ""),
    65: TownTrait("Well-Defended", ""),
    66: TownTrait("Unique Location", ""),
}
