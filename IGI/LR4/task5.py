# In accordance with the assignment of your option, explore the capabilities of the NumPy library when working with arrays and mathematical and static operations.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich.
# 08.04.2024.

import TaskClass
import input_checker, repeater
import numpy as np, random, statistics, math

class Task5(TaskClass.Task):
    
    def __init__(self, task):
        """A function that initializes a class object."""
        super().__init__(task)
        self.arr = None

    def start_task(self):
        """A function that performs the main task."""
        rep = True
        while rep:

            n = input_checker.int_check('Enter the size of the matrix length: \n', 0, 100)
            m = input_checker.int_check('Enter the matrix width size: \n', 0, 100)
            self.arr = np.array([[random.randint(-100, 100) for i in range(n)] for j in range(m)])
            print('Matrix:')
            print(self.arr)
            print(f'\nSum of elements below the main diagonal: {self.sum_under_diag()}\n')
            print(f'The standard deviation of the main diagonal, calculated using the numpy method: {round(self.std(), 2)}\n')
            print(f'The standard deviation of the main diagonal, calculated manually: {round(self.custom_std(), 2)}\n')

            rep = repeater.repeater()

    def sum_under_diag(self):
        """A function that calculates the sum of elements below the main diagonal."""
        return sum([sum(elem for index2, elem in enumerate(elems) if index1 > index2) for index1, elems in enumerate(self.arr)])
    
    def std(self):
        """A function that calculates the standard deviation of the main diagonal."""
        return np.std([self.arr[i][i] for i in range(min(self.arr.shape))])

    def custom_std(self):
        """A function that calculates the standard deviation of the main diagonal manually."""
        elems = [self.arr[i][i] for i in range(min(self.arr.shape))]
        aver = statistics.mean(elems)
        return math.sqrt(sum([(elem - aver) ** 2 for elem in elems]) / len(elems))
        