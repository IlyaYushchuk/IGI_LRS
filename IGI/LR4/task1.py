# Serialize the dictionary and calculate the corresponding data as specified.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich
# 8.04.2024.

import TaskClass
import datetime
import pickle, csv
import input_checker, repeater

class Task1(TaskClass.Task):
    
    def __init__(self, task):
        """Function initialize class object."""
        super().__init__(task)
        self.class_dict = {"Petrov A.A.": datetime.date(2006,2,15),
                            "Ivanov V.K.": datetime.date(2006,2,2),
                            "Grigoriev E.H.": datetime.date(2005,12,29)}

    @property
    def dict_init(self):
        return self.class_dict
    
    @dict_init.setter
    def dict_init(self, new_list):
        self.class_dict = new_list

    def start_task(self):
        """Function give ability to interact with class."""
        rep = True
        while rep:
            self.curr_task(self.current_task)
            rep_inside = True
            while rep_inside:
                action = input_checker.int_check('Choose activity\n'+
                                                 '1)Get pupils by month\n'+
                                                 '2)Get pupils from file with CSV\n'+
                                                 '3)Set pupils in file with CSV\n'+
                                                 '4)Get pupils from file with pickle\n'+
                                                 '5)Set pupils in file with pickle\n'+
                                                 '6)Exit\n', 1, 6)
                match action:
                    case 1:
                        month = input_checker.int_check('Choose month ', 1, 12)
                        print(self.select_pupils_by_birth_month(month))
                    case 2:
                        self.get_CSV()
                        print(self.class_dict)
                    case 3:
                        self.set_CSV()
                    case 4:
                        self.get_pickle()
                        print(self.class_dict)
                    case 5:
                        self.set_pickle()
                    case 6:
                        rep_inside = False
                print()
            rep = repeater.repeater("Task 1:")


    def select_pupils_by_birth_month(self, month):
        """Function return list of pupils with selected month"""
        pupils = dict()
        for key in self.class_dict.keys():
            if self.class_dict[key].month == month:
                pupils[key] = self.class_dict[key]
        return pupils

    def get_pickle(self):
        """A function that reads data from a file using pickle."""
        with open('task1.txt', 'rb') as file:
            self.class_dict = pickle.load(file)

    def set_pickle(self):
        """A function that writes data to a file using pickle."""
        with open('task1.txt', 'wb') as file:
            pickle.dump(self.class_dict, file)
        
    def set_CSV(self):
        """A function that writes data to a file using CSV."""
        with open('task1.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for key, value in self.class_dict.items():
                writer.writerow([key, value])
        
    def get_CSV(self):
        """A function that reads data from a file using CSV."""
        with open('task1.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                list =[int(s) for s in row[1].split('-')]
                #print(list)
                self.class_dict[row[0]] = datetime.date(*list)

