'''
Given a string, find the start position of the largest block of repeated characters.
'''

def largest_block(str):
	if len(str) < 2:
		return 0
	# stores in form: [char, index, length]
	result = [str[0], 0, 1]
	current = [str[0], 0, 1]
	for i in xrange(1, len(str)):
		char = str[i]
		if char == current[0]:
			current[2] += 1
			if current[2] > result[2]:
				result = current
		else:
			current = [char, i, 1]
	return result[1]


if __name__ == '__main__':
	print largest_block("aaabbccccddeeeeee")
