#!/usr/bin/python3
'''
creates an object from a "JSON file"
'''
import json


def load_from_json_file(filename):
    '''
    creates an object from a "JSON file"
    '''
    try:
        with open(filename, encoding='utf_8') as f:
            obj = f.read()
            json_obj = json.loads(obj)
    except FileNotFoundError:
        with open(filename, 'w+', encoding='utf_8') as f:
            json_obj = json.loads(obj)
        return json_obj
