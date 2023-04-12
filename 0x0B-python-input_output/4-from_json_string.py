#!/usr/bin/python3
"""
4-from_json_string
Function that returns an object (Python data structure) represented by a JSON string
"""
def from_json_string(my_str):
    import json

    return json.loads(my_str)
