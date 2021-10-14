#!/usr/bin/python3
'''
creates an object from a "JSON file"
'''
import json


def load_from_json_file(filename):
    '''
    creates an object from a "JSON file"
    '''
    with open(filename, 'r+') as f:
        obj = f.read()
        json_obj = json.loads(obj)
    return json_obj
