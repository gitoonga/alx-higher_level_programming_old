#!/usr/bin/python3
"""
3-write_file

function that writes to a text file (utf-8) and returns the number of characters written
"""

def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8" as file:
            return(file.write(text))
