# In the line entered from the keyboard, count the number of number-characters.
# Lab 3.
# Standard data types, collections, functions, modules.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich
# 27.03.2024.

import repeater
import time

def task():
    """A function that counts the number of digits in a string."""
    rep = True
    while rep:
        input_string = input('Enter the string: \n')
        number_character_count(input_string)
        rep = repeater.repeater('Task 3')

def print_answer(func):
    """A decorator function that prints the response to the console."""
    def wrapper(*args, **kwargs):
        start = time.time()
        original = func(*args, **kwargs)
        end = time.time()
        print(func.__name__)
        print('The function worked in', end - start)
        for i in range(10):
            print('Quantity of',i,'in string:', original[i])
        
    return wrapper

@print_answer
def number_character_count(original_string):
    """A function that counts digits in a string."""
    try:
        numbers = [0,0,0,0,0,0,0,0,0,0]
        for char in original_string:
            if char >= '0' and char <= '9':
                numbers[int(char)] += 1
        return numbers
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')