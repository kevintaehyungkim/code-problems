'''
Write a function to find the longest common prefix string amongst an array of strings.

Difficulty: Easy

Solution notes:
Taking advantage of Python's builtin all() function, which returns true if a condition is true 
for all elements in a list.

O(n*m) time where n is the number of words and m is the length of the longest prefix
O(1) space
'''

def longestCommonPrefix(self, strs):
	if not strs:
		return ""
	ans = ""
	shortest = min(len(s) for s in strs)
	# iterate through length of shortest word
	for i to xrange(shortest):
		# iterates through letters of first word
		letter = strs[0][i]
		# for each letter, if it equals every other letter in the array, append to answer
		if all(s[i] == letter for s in strs):
			ans += letter
		else:
			break
	return ans
