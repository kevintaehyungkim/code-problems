'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Difficulty: Easy

Solution notes:

'''

# int (x, b) returns value of bit string x in base b
# bin(x) returns the binary string representation of an integer x, we cut off the leading '0b'

def add_binary(a, b):
	sum = int(a,2) + int(b,2)
	return bin(sum)[2:]
