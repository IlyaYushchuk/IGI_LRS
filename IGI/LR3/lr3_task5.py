# the program implements work with sequences and also provides a search for minimal elements.
# Lab 3.
# Standard data types, collections, functions, modules.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich
# 27.03.2024.

import repeater
import inputsequence
import input_checker
import math

def task():
    """A function that find maximum modulo element and multiplication of elements between the first two zero elements."""
    rep = True
    while rep:
        print('Select the sequence input method:\n1. Generator function\n2. Manual input\n')
        var = input_checker.int_check(1, 2)
        list = []
        if var == 1:
            gen = inputsequence.seq_input()
            for num in gen:
                list.append(num)
        elif var == 2:
            list = inputsequence.user_input()
        max_abs_index = max_abs_elem_index(list)
        multip = mul_between_two_zeros(list)
        print('Index of the maximum modulo element:', max_abs_index)
        if multip is not None:
            print('Multiplication of elements between the first two zero elements:', multip)
        else:
            print('There are no two zero elements in the sequence')
        print(list)
        rep = repeater.repeater('Task 5')

def max_abs_elem_index(list):
    """A function that find the index of the maximum modulo element"""
    try:
        index_max = -1
        max = 0
        for i in range(len(list)):
            if abs(list[i]) > max:
                max = abs(list[i])
                index_max = i
        if index_max == -1:
            index_max = None
        return index_max
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')

def mul_between_two_zeros(list):
    """A function that find the multiplication of the elements between the first two zero elements."""
    try:
        first_zero_index = -1
        second_zero_index = -1
        for i in range(len(list)):
            if list[i] == 0:    
                if first_zero_index < 0:
                    first_zero_index = i
                elif second_zero_index < 0:
                    second_zero_index = i
        mul_elems = math.prod(list[first_zero_index + 1:second_zero_index])
        if second_zero_index == -1:
            mul_elems = None
        return mul_elems
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
