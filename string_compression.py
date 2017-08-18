'''
From: Cracking the Coding Interview 6th ed. #1.6

Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2bc5a3. 

If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).

Difficulty: Easy

Solution notes:
O(n) time
O(n) space
'''

def string_compression(string):

	if len(string) == 0:
		return
	elif len(string) == 1:
		return string[0]

	letter = string[0]
	count = 0
	ret = ""
	
	for s in string:
		if s == letter:
			count += 1
		else:
			if count == 1:
				ret += letter
				letter = s
			else:
				ret += letter + str(count)
				letter = s
				count = 1
	ret += letter + str(count)

	return ret


if __name__ == '__main__':
  print string_compression("aabcccccaaa")
  