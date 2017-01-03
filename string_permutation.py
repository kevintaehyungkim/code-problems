'''
Print all permutations of a string.

Difficulty: Easy

Solution notes:
O(n*n!) time
O(1) space
'''

def string_permutation(string, prefix = ''):
	if len(string) == 0:
		print prefix
	else:
		for s in string:
			string_permutation(string[:string.index(s)]+string[string.index(s)+1:], prefix + s)



if __name__ == '__main__':
  print string_permutation("abc", '')