# In accordance with the instructions of your option, modify the program from LR3 using the class.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich.
# 08.04.2024.

import TaskClass
import input_checker, repeater
import math, statistics, matplotlib.pyplot as plt

class Task3(TaskClass.Task):
    
    def __init__(self, task):
        """A function that initializes a class object."""
        super().__init__(task)

    def start_task(self):
        """A function that performs the main task."""
        rep = True
        while rep:

            eps = input_checker.float_check('\nEnter the calculation precision eps:\n', 0, float('inf'))
            x = input_checker.float_check('\nEnter x in the range -1 to 1:\n', -1, 1)

            ans, n, list = self.my_ln(x, eps)
            print('Manually calculated result:', ans)
            print('Calculated result using the math module: ', math.log(1 - x))
            print('Number of iterations: ', n)
            print(f'Arphimetic mean of list elements: {statistics.mean(list)}')
            print(f'Median of list elements: {statistics.median(list)}')
            print(f'List item mode: {statistics.mode(list)}')
            print(f'Variance of list elements: {statistics.variance(list)}')
            print(f'Standard deviation of list elements: {statistics.stdev(list)}')
            self.draw(5)

            rep = repeater.repeater("Task 3:")

    def my_ln(self, x, eps):
        """A function that calculates the natural logarithm for a given argument and precision."""
        try:
            fx = 0
            n = 500
            list = []
            for i in range(1, 501):
                prev = fx
                fx = -(x ** i / i)
                list.append(fx)
                if abs(fx - prev) <= eps:
                    n = i - 1
                    return (sum(list), n, list)
        except ValueError:
            print('ValueError')
        except TypeError:
            print('TypeError')
    
    def draw(self, h):
        """A function that constructs a graph with variant functions."""
        eps = input_checker.float_check('\nEnter the accuracy of the eps calculations for plotting:\n', 0, 1)
        x = [i / 101 for i in range(-100, 100, h)]
        my_y = [self.my_ln(elem, eps)[0] for elem in x]
        math_y = [math.log(1 - elem) for elem in x]
        
        dif_list = []

        for i in zip(my_y.copy(), math_y.copy()):
            dif_list.append(abs(i[0] - i[1]))
            #print(abs(i[0] - i[1]))
        
        max_dif = 0
    
        for value in dif_list:
            if value > max_dif:
                max_dif = value
        
        index = dif_list.index(max_dif)
        i = x[index]
        j = my_y[index] 

        #print(f'i {i} j {j}')
        fig, ax = plt.subplots()

        ax.plot(x, my_y, 'red', linewidth=2, label='Taylor')
        ax.plot(x, math_y, 'blue', linewidth=2, label='Math')
        ax.legend(loc='best')
        ax.set_xlabel('Ox')
        ax.set_ylabel('Oy')
        plt.title("Taylor vs Math module")
        #ax.text(-1.05, -2.3, 'Taylor vs Math module')
       
        ax.annotate('Max diff point', xy=(i, j), xytext=(i - 0.3, j - 0.3), arrowprops=dict(facecolor='green', shrink=0.01))
        plt.savefig('task3_pic.png')
        plt.show()