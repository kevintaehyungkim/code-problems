Amazon


Dictionary of words. Pattern. We need to find all teh words in the dictionary that match the given pattern.

Dictionary: [‘ABC’ , ‘AMM’, ‘MNN’, ‘AQA’]
Pattern: ['ABB']
pattern mnm
ABC => [0 1 2] [A, B, C] 

def find_pattern (my_dict, pattern):
    if len(pattern) == 0: 
        return False
    pattern_array = []
    for i in range (0,len(entry)-1):
            if entry[i:i+1] in entry_array:
                index = 0
                
            else:
                entry_array.append(letters_used)
                letters_used += 1
    entry_array = []
    for entry in my_dict:
        if len(entry) != len(pattern):
            return False
        entry_array = []
        letters_used = 0
        for i in range (0,len(entry)-1):
            if entry[i:i+1] in entry_array:
                # get index of first time its seen, and append that value to array
            else:
                entry_array.append(letters_used)
                letters_used += 1
    for i in range(0, len(pattern)):
        if pattern_array[i] != entry_array[i]:
            return False
    return True
            
                
                
                
                AQA = 121
                ABB = 122
                MNM = 121
                
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
 
 class Card 
 variables: my_number (int)  
             my_type (String)
      
Class Deck:             
array that holds Card objects 
functions put buttom: index 0
            draw: index len(arr) -1 
pop 
 
                
                
                
            
            