#!/usr/bin/env python3

"""
Exercise from chapter seven

A program that checks if a given password is strong. A strong password has the following:

    1. Eight characters long
    2. Contains both uppercase and lowercase characters
    3. Has atleast one digit
"""

import re

__author__ = "Alex DeCesare"
__version__ = "24-August-2020"

def check_strength(password):
    """
    checks if the inputted password is strong

    arguments:
    password -- the specified password to check
    """

    is_strong = True
    if len(password) < 8:
        is_strong = False

    upper_case = re.compile(r'[A-Z]')

    if not upper_case.search(password):
        is_strong = False

    lower_case = re.compile(r'[a-z]')

    if not lower_case.search(password):
        is_strong = False

    numeric_pattern = re.compile(r'[1-9]')

    if not numeric_pattern.search(password):
        is_strong = False


    state = 'strong' if is_strong else 'not strong'
    print('your password is ' + state)
def main():

    """
    Launches the stript
    """

    print("Please type a password")
    password = input()
    check_strength(password)

if __name__ == '__main__':
    main()
