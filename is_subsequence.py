'''
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. 
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
s = "abc", t = "ahbgdc"
Return true.
Example 2:
s = "axc", t = "ahbgdc"
Return false.
Difficult: Medium
'''

def is_subsequence(s,t):
	# basic checks
	if len(s) > len(t):
		return False
	elif s == t or len(s) == 0:
		return True

	res = ""
	s_idx = 0

	while t:
		if s[s_idx] == t[0]:
			res += t[0]
			s_idx += 1
		t = t[1:]
		if s_idx == len(s):
			break
			
	if res == s:
		return True
	return False


if __name__ == '__main__':
	print is_subsequence("abc", "ahbgdc")

  
