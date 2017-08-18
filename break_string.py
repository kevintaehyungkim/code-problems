'''
Given a string and dictionary of words, break the string in minimum space sentence

ex. inputString = "ilikefacebook"
dictionary = {"i", "like", "face", "book", "facebook"}
possible stings: 
	i like face book
	i like facebook (expected answer)

Questions: will the dictionary contain every use of the word in the string?
'''

def break_string(input_str, word_dict):
	if not input_str:
		return None
	elif not word_dict:
		return input_str
	oldStr = input_str
	newStrArr = []
	while oldStr:
		low = 0
		high = len(oldStr)
		while low < high:
			print oldStr[low:high]
			if oldStr[low:high] in word_dict:
				newStrArr.insert(0, oldStr[low:high])
				oldStr = oldStr[0:low]
			else:
				low += 1
	return ' '.join(newStrArr)

if __name__ == '__main__':
	print break_string("ilikefacebook", ["i", "like", "face", "book", "facebook"])



