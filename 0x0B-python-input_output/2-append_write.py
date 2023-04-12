#!/usr/bin/python3

"""
2-append_write
Function that appends a string at the end of a file(utf-8) and returns the number of characters added
"""

def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as file:
        return(file.write(text))
