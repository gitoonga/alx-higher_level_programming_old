#!/usr/bin/python3
"""
load_from_json_file

Function that creates an Object from a “JSON file”
"""
def load_from_json_file(filename):
    import json

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
