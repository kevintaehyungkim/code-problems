'''
Given a string of words, truncate to only 10 characters that includes only full words
'Max runtime would be length of word m: O(m) as opposed to iterating through n words until index 10, or O(n)
'''

def truncate_string(s):
	index = 9
	if len(s) <= 10:
		return s
	elif s[index] == ' ':
		return s[:index]
	else:
		while s[index] != ' ':
			index -= 1
	return s[:index]



if __name__ == '__main__':
	print truncate_string("abc deghi jkl mno pqr")