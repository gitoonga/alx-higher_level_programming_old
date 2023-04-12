#!/usr/bin/python3
"""
7-save_to_json_file

Function that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
