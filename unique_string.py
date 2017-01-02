'''
implement an algorithm to determine if a string has all unique characters 
w/o additional data structures

Difficulty: Easy

Solution notes:
O(n^2) / O(n) time
O(1) / O(1) space

'''

#length of ASCII alphabet = 128

def unique_string(string):
	if len(string) > 128:
		return False
	char_array = [0]*128
	for char in string:
		if char_array[ord(char)] == 1:
			return False
		else
			char_array[ord(char)] == 1
	return True
