#!/usr/bin/env python3
'''
    Charts

'''

import json

HC = True
# HC_DATAFILE = 'hexcrawl.json'
HC_DATAFILE = 'hexcrawl_fake.json'

TOWN_TRAITS = None
JOBS_BOARD = None
TERRAIN_ENCOUNTERS = None
INJURY = None
MADNESS = None
MUTATION = None


def obj_hook(dct):
    '''
    Used by json.load(s), this function replaces any keys from decoded JSON
    that look like integers with actual integers.
    This is so values can be retrieved directly by their dice rolls, instead of
    converting to string first.

    '''
    new_dct = dict()
    for key, val in dct.items():
        try:
            key = int(key)
        except (ValueError, TypeError):
            pass
        new_dct[key] = val
    return new_dct


if HC:
    with open(HC_DATAFILE) as file_in:
        DATA = json.load(file_in, object_hook=obj_hook)

    for key, val in DATA.items():
        exec('{} = {}'.format(key.upper(), val))
