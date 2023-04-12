#!/usr/bin/python3
"""
0-read_file

Function to read and print contents of file
"""

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8" as file:
            print(file.read(), end="")
