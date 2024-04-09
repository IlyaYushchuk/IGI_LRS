# A program that involves working with text implements the solution of three subtasks according to options.
# Lab 3.
# Standard data types, collections, functions, modules.
# v 1.0.0.
# Yushchuk Ilya Alexandrovich
# 27.03.2024.

import repeater

def task():
    """A function that performs the main task."""
    rep = True
    while rep:
        original_string = 'So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.'
        words_list = original_string.replace(',', '').strip('.').lower().split(' ')
        descent_list = display_words_descend_order(words_list)
    
        print('1. Number of words with less than 7 characters:', finding_num_of_words_less_than_7(words_list))
        print('2. The shortest word ending with the letter "a": ', finding_shortest_word_ended_a(words_list))
        print('3. Descenting list of word:\n',descent_list)

        rep = repeater.repeater('Task 4')

def finding_num_of_words_less_than_7(word_list):
    """A function that counts words that are less than 7 characters long."""
    try:
        count = 0
        for word in word_list:
            if len(word) < 7:
                count += 1
        return count
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')

def finding_shortest_word_ended_a(word_list):
    """A function that searches for the shortest word that ends in 'a'."""
    try:
        cur_min = ''
        for word in word_list:
            if (word.endswith('a') and len(cur_min) > len(word)) or len(cur_min) == 0:
                cur_min = word
        return cur_min
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')

def display_words_descend_order(word_list):
    """A function that displays words of text in descending order."""
    try:
        descent_list = sorted(word_list, key=len, reverse=True)
        return descent_list
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')