# In accordance with the specifications of your variant, develop base classes and descendant classes.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich.
# 08.04.2024.

from abc import ABC, abstractmethod
import math
import TaskClass
import repeater, input_checker
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Color():
    def __init__(self, color):
        """A function that initializes a class object."""
        self.color = color

    @property
    def color_init(self):
        """Getter function for the color variable."""
        return self.color
    
    @color_init.setter
    def color_init(self, new_color):
        """Setter function for the color variable."""
        self.color = new_color

    @color_init.deleter
    def x(self):
        """Deleter function for the color variable."""
        del self.color

    def __str__(self):
        """Magic method that overrides __str__."""
        return self.color

class Geometric_figure(ABC):

    @abstractmethod
    def square(self):
        """A function that calculates the area of ​​a figure."""

class Regular_n_gon(Geometric_figure):

    def __init__(self, name, length, n, color):
        """A function that initializes a class object."""
        super().__init__()
        self.n = n
        self.length = length
        self.color = Color(color)
        self.name = name

    @property
    def get_n(self):
        """Getter function for variable n."""
        return self.n
    
    @get_n.setter
    def set_n(self, new_n):
        """Setter function for variable n."""
        self.n = new_n
    @property
    def get_length(self):
        """Getter function for the length variable."""
        return self.length
    
    @get_length.setter
    def set_length(self, new_length):
        """Setter function for the length variable."""
        self.length = new_length

    @property
    def get_name(self):
        """Функция-геттер для переменной name."""
        return self.name
    
    @get_name.setter
    def set_name(self, new_name):
        """Setter function for the name variable."""
        self.name = new_name

    def square(self):
        """An overridden function that calculates the area of ​​a square."""
        return self.n / 4 * self.length**2 * 1 / math.tan(math.pi/self.n)
    
    def draw(self, text):
        """The function draws a regular n-gon with side a."""
        try:
            fig, ax = plt.subplots()
            radius = self.length / (2 * math.sin(math.pi/(2*self.n)))
            #print(f'radius {radius}')
            dots = []
            for i in range(self.n):
                #print(((math.pi * 2 * i)/self.n) * 180 / math.pi)
                dots.append((radius*math.cos((math.pi * 2 * i)/self.n),radius*math.sin((math.pi * 2 * i)/self.n)))
                
            #print(dots)
            polygon = patches.Polygon(dots, facecolor = str(self.color))
            
            ax.add_patch(polygon)
            plt.xlim(-self.length * self.n/2, self.length * self.n/2)
            plt.ylim(-self.length * self.n/2, self.length * self.n/2)
            plt.gca().set_aspect('equal')
            plt.title(text)
            plt.savefig('task4.png')
            plt.show()
        except ValueError:
            print('Incorrect color')
            plt.close()
    
    def __str__(self):
        """Magic method that overrides __str__."""
        return 'Regular {}-polygon side length: {}\nPolygon square {}\nPolygon color: {}'.format(self.n ,self.length, self.square(), str(self.color))

class Task4(TaskClass.Task):
    def __init__(self, task):
        """A function that initializes a class object."""
        super().__init__(task)

    def start_task(self):
        """A function that performs the main task."""
        rep = True
        while rep:

            name = input('Enter the name of the figure:\n')
            length = input_checker.float_check('Input length of a:\n', 0, float('inf'))
            color = input('Enter the color of the square:\n')
            text = input('Enter a caption for the picture:\n')
            n = input_checker.int_check('Input n:\n',3,100)
            pol = Regular_n_gon(name, length, n, color)
            #rect = Regular_n_gon("lox", 2, 5, "green")
            
            pol.draw(text)
            print(pol.__str__())
            rep = repeater.repeater("Task 4: ")