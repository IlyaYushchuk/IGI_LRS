# Create a loop that takes integers and count number of elements which bigger than 12.
# Lab 3.
# Standard data types, collections, functions, modules.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich
# 27.03.2024.

import repeater
import input_checker

def task():
    """A function that calculates the number of elements greater than 12."""
    repeat = True
    print('The program calculates the number of elements in a sequence greater than 12.\nEnter sequential integers. To finish entering the sequence, enter 133')
    while repeat:
        ans = find_num_of_elements()
        print('The number of elements is more than 12', ans)
        repeat = repeater.repeater('Task 2')

def find_num_of_elements():
    """A function that takes integers in a loop and counts the number of elements greater than 12."""
    try:
        num_of_elem = 0
        rep = True
        while rep:
            print('\nEnter an integer')
            curr = input_checker.int_check()
            if curr == 133:
                rep = False
            elif curr > 12:
                num_of_elem += 1
        return num_of_elem
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')