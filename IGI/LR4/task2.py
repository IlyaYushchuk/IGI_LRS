# In accordance with the assignment of your option, create a program for text analysis.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich.
# 08.04.2024.

import TaskClass
import input_checker, repeater
import re
from zipfile import ZipFile

class Task2(TaskClass.Task):
    
    filename = 'task2.txt'
    text = ''

    def __init__(self, task):
        """A function that initializes a class object."""
        super().__init__(task)

    @property
    def filename_init(self):
        """Getter function for the filename variable."""
        return self.filename
    
    @filename_init.setter
    def dict_init(self, new_filename):
        """Setter function for the filename variable."""
        self.filename = new_filename

    @property
    def text_init(self):
        """Getter function for the text variable."""
        return self.filename
    
    @text_init.setter
    def text_init(self, new_text):
        """Setter function for the text variable."""
        self.text = new_text

    def start_task(self):
        """A function that performs the main task."""
        rep = True
        while rep:
            
            self.get_text()
            self.general_task()
            self.variant_task()
            self.zip_result_file()
            print(self.find_file_info_in_zip("task2_resaults.txt"))
            

            rep = repeater.repeater("Task 2:")
            
    def get_text(self):
        """A function that reads data from a file."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.text = file.read()
    
    def general_task(self):
        """A function that writes the results of a shared job to a file."""
        with open('task2_resaults.txt', 'w', encoding='utf-8') as file:
            file.write(f'General tasks\n\n')
            file.write(f'Number of sentences in text: {self.find_sentence_count()}\n')
            type_count = self.find_sentence_type_count()
            file.write(f'\tNarrative: {type_count[0]}\n')
            file.write(f'\tIncentive: {type_count[1]}\n')
            file.write(f'\tInterrogative: {type_count[2]}\n')
            file.write(f'Average sentence length: {self.find_average_sentence_len()}\n')
            file.write(f'Average word length: {self.find_average_word_len()}\n')
            file.write(f'Number of emoticons in the text: {self.find_smiles_count()}\n')
            

    def variant_task(self):
        """A function that writes the results of specifying a variant to a file."""
        with open('task2_resaults.txt', 'a', encoding='utf-8') as file:
            file.write('\nOption 29 tasks\n\n')
            file.write('Words with lower case and numbers:\n')
            for word in self.find_lower_case_digits_words():
                file.write(f'{word}\n')
            file.write('IP adresses:\n')
            for ip in self.find_ip_adresses():
                file.write(f'{ip}\n')
            file.write('Number of loser case letters: ')
            file.write(f'{self.find_number_of_losercase_letters()}\n')
            file.write('First word with \'v\' letter and its number:\n')
            file.write(f'Word: {self.find_word_with_v_letter()[0]}\nNumber: {self.find_word_with_v_letter()[1]}\n')
            file.write('Text without s-start words\n')
            file.write(f'{self.find_test_without_s_words()}')

#----------basic functions-------------------
    def find_sentence_count(self):
        """A function that counts the number of sentences in a text."""
        return len(re.findall(r'[\.!?]', self.text))
    
    def find_sentence_type_count(self):
        """A function that counts the number of sentences of different types."""
        list = re.findall(r'[\.!?]', self.text)
        return (list.count('.'), list.count('!'), list.count('?'))
    
    def find_average_sentence_len(self):
        """A function that calculates the average length of a sentence in characters."""
        return sum(len(elem) for elem in re.findall(r'\w+', self.text)) / self.find_sentence_count()
    
    def find_average_word_len(self):
        """A function that calculates the average length of a word in a text in characters."""
        list = re.findall(r'\w+', self.text)
        return sum(len(elem) for elem in list) / len(list)
    
    def find_smiles_count(self):
        """A function that counts the number of emoticons in the text."""
        return len(re.findall(r'[:;]-*(\)+|\(+|\]+|\[+)', self.text))
    
    def zip_result_file(self):
        with ZipFile("zipped_result.zip","w") as zip_file:
            zip_file.write("task2_resaults.txt")
            zip_file.write("task2.txt")
            

    def find_file_info_in_zip(self, file):
        with ZipFile("zipped_result.zip","r") as zip_file:
            return zip_file.getinfo(file)
#----------end of basic functions------------------

#----------special functions-----------------------

    def find_lower_case_digits_words(self):
        """The function finds words with lowercase letters and numbers"""
        #TODO make function better
        words = re.findall(r'\b[a-z]+\d+\w*\b', self.text)
        return words

    def find_ip_adresses(self):
        """The function finds IP addresses in text"""
        ip_adresses = re.findall(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b',self.text)
        return ip_adresses

    def find_number_of_losercase_letters(self):
        """The function finds finds the number of lowercase letters"""
        list_of_lowercase = re.findall(r'[a-z]', self.text)
        return len(list_of_lowercase)
    
    def find_word_with_v_letter(self):
        """The function finds the first word with the symbol v and its number"""
        all_words = re.findall(r'\w+', self.text)
        for index, word in enumerate(all_words):
            if 'v' in word:
               return word, index + 1 
            
    def find_test_without_s_words(self):
            """The function returns text without words starting with s."""
            text = self.text
            s_words = re.findall(r'\b([sS][\w]*)\b', self.text)
            for word in s_words:
                text = text.replace(word, '')
            return text
   