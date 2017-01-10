'''
Cracking the Coding Interview
1.9: Assume you have a method isSubstring which checks if one word is a substring of another.
Given 2 strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring.

ex. "waterbottle" is a rotation of "erbottlewat"
'''

def is_rotation(s1,s2):
	if len(s1) != len(s2):
		return False
	elif s1 == s2:
		return True
	else:
		for i in xrange(0, len(s1)):
			s2 = s2[1:] + s2[0]
			if s1 == s2:
				return True
	return False


if __name__ == '__main__':
  print is_rotation("waterbottle", "erbottlewat")

