# Calculate the value of a function with a given accuracy.
# Lab 3.
# Standard data types, collections, functions, modules.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich
# 27.03.2024.


import input_checker
import repeater
import math

def task():
    """A function that performs the calculation of the ln(1-x) function with a predefined precision."""
    rep = True
    while rep:
        print('\nEnter the accuracy of calculations:')
        eps = input_checker.float_check(0, 0.1)
        print('\nEnter a value for x in the range from -1 to 1:')
        x = input_checker.float_check( -1, 1)

        res = custom_ln(x, eps)

        print('The result of the custom_ln function:', res[0])
        print('The result of the function from the math module:', math.log(1 - x))
        print('Number of iterations:', res[1])
        rep = repeater.repeater('Task 1')

def custom_ln(x, eps):
    """A function that calculates the natural logarithm with a specified accuracy."""
    try:
        fx = 0
        n = 500
        for i in range(1, 501):
            prev = fx
            fx -= x ** i / i
            if abs(fx - prev) <= eps:
                n = i - 1
                return (fx, n)
    except ValueError:
        print('ValueError has been catched')
    except TypeError:
        print('TypeError has been catched')