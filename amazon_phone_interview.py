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


Dictionary of words. Pattern. We need to find all teh words in the dictionary that match the given pattern.

Dictionary: [‘ABC’ , ‘AMM’, ‘MNN’, ‘AQA’]
Pattern: ['ABB']
pattern mnm
ABC => [0 1 2] [A, B, C] 

AQA = 121
ABB = 122
MNM = 121
'''

def find_pattern (my_dict, pattern):
    if len(pattern) == 0: 
        return False

    pattern_array = []
    num_letters = 0
    letter_dict = {}
    for i in range (0,len(pattern)-1):
        letter = pattern[i:i+1]
        if letter in pattern_array:
            pattern_array.append(letter_dict[letter])
        else:
            pattern_array.append(num_letters)
            num_letters += 1
            letter_dict[letter] = num_letters

    entry_array = []
    for entry in my_dict:
        if len(entry) != len(pattern):
            return False
        entry_array = []
        letters_used = 0
        entry_dict = {}
        for i in range (0,len(entry)-1):
            letter = entry[i:i+1]
            if letter in entry_array:
                entry_array.append(letter_dict[letter])
            else:
                entry_array.append(letters_used)
                letters_used += 1
                entry_dict[letter] = letters_used
        if pattern_array == entry_array:
            return True
            
    return False



if __name__ == '__main__':
    print find_pattern(["ABC" , "AMM", "MNN", "AQA"], "ABB")
            