'''
From: Cracking the Coding Interview 6th ed. #1.6

Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.

If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).

Difficulty: Easy

Solution notes:
O(n) time
O(n) space
'''

def string_compression(string):

	letter = string[0]
	count = 0
	ret = ""
	
	for s in string:
		if s == letter:
			count += 1
		else:
			ret += letter + str(count)
			letter = s
			count = 1

	if len(ret) > len(string):
		return string

	return ret


if __name__ == '__main__':
  print string_compression("aabcccccaaa")
  