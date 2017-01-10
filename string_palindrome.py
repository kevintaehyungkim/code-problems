'''
Cracking the Coding Interview
1.4: Given a string, write a function to check if it's a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just 
dictionary words.

ex: "taco cat" -> true
'''

def string_permutation(str):
	if not str:
		return True
	new_str = ''.join(word for word in str.split(' '))
	first_half = second_half = ""
	length = len(new_str)
	# odd length
	if len(new_str) % 2:
		first_half = new_str[0:(length/2)]
		second_half = new_str[(length/2)+1:length]
	# even length
	else:
		first_half = new_str[0:length/2]
		second_half = new_str[length/2:length]
	# reverse 2nd half
	second_half = second_half[::-1]
	# compare both halves
	if first_half == second_half:
		return True
	return False


if __name__ == '__main__':
  print string_permutation("!taco cat!")
