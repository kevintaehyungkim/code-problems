# -*- coding: utf-8 -*-
# Amazon Phone Interview 2017
'''
 How do you print out the nodes of a binary tree in level-order?  
 
     1
   2    3
 4  5  6  7
   
   123
   
   Queue: 1
   Queue: 2,3    
   
 
 Design a generic deck of cards which can be used for different games - Poker, Blackjack etc. 
 What are the classes that you will need? Data members/functions.
 (Object oriented principles)     
 
Class Card:
variables: my_number (int)
           my_type (String)
     
Class Deck:         
array that holds Card objects
functions -
put buttom: index 0
draw: index len(arr) -1
push or pop


Dictionary of words. Pattern. We need to find all the words in the dictionary that match the given pattern.

Dictionary: [‘ABC’ , ‘AMM’, ‘MNN’, ‘AQA’]
Pattern: 'ABB'
pattern mnm
ABC => [0 1 2] [A, B, C]

AQA = 121
ABB = 122
MNM = 121
'''

def find_pattern (my_dict, pattern):
    if len(pattern) == 0: 
        return False

    result = []

    pattern_array = []
    num_letters = 0
    letter_dict = {}

    for letter in pattern:
        if letter in letter_dict.keys():
            pattern_array.append(letter_dict[letter])
        else:
            pattern_array.append(num_letters)
            letter_dict[letter] = num_letters
            num_letters += 1

    for entry in my_dict:
        if len(entry) != len(pattern):
            continue
        entry_array = []
        letters_used = 0
        entry_dict = {}
        for letter in entry:
            if letter in entry_dict.keys():
                entry_array.append(entry_dict[letter])
            else:
                entry_array.append(letters_used)
                entry_dict[letter] = letters_used
                letters_used += 1
        if pattern_array == entry_array:
            result.append(entry)
            
    return result


if __name__ == '__main__':
    print find_pattern(["ABC" , "AMM", "MNN", "AQA"], "ABB")
            