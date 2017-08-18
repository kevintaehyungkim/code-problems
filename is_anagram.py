'''
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Difficult: Easy

Solution Notes:
O(n) time
O(1) space
'''

def is_anagram(s,t):
	letter_dict = {}
	for letter in s:
		if letter in letter_dict:
			letter_dict[letter] = letter_dict[letter] + 1
		else:
			letter_dict[letter] = 1
	for letter in t:
		letter_dict[letter] = letter_dict[letter] - 1 
	for val in letter_dict.values():
		if val != 0:
			return False 
	return True

if __name__ == '__main__':
  print is_anagram("anagram", "nagaram")