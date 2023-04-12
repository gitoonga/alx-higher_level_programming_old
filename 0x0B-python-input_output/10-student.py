#!/usr/bin/python3
"""
Class Student that defines a student by: (based on 9-student.py)
"""


class Student():
    """
    Public Instance Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with first name, last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
    """
    If attrs is a list of strings, only attribute names contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved
    """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
