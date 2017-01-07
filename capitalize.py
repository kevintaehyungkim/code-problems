'''
You are given a string . Your task is to capitalize each word of .

Input Format:
A single line of input containing the string, .

Constraints:
The string consists of alphanumeric characters and spaces.

Sample Input: hello world
Sample Output: Hello World
'''

def capitalize(string):
	return ' '.join([word.capitalize() for word in string.split()])