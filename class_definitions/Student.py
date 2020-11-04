"""
Author: Alex Alvarado
Date: 10-31-20
Program: Student.py
Description: Student class which uses Student information
"""


class Student:
    """Student Class"""

    MAJORS = ['Spells', 'English', 'Chem', "CompSci", 'Literature',
              'Political Science', 'Necromancy']

    def __init__(self, lname, fname, major, gpa=0.0):
        """
        :param lname: String
        :param fname: String
        :param major: String
        :param gpa: Float
        """

        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError

        if major not in self.MAJORS:
            raise ValueError
        if not 0.0 <= gpa <= 4.0:
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        """
        :return: String
        """
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

