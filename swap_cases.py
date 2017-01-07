'''
You are given a string s. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
'''

# strings are immutable, so create new string as you iterate through input string
def swap_cases(s):
	new_string = ""
	for char in s:
		new_string += char.swapcase()
	return new_string