'''
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:
["((()))", "(()())", "(())()", "()(())", "()()()"]

Difficulty: Medium
'''

def generate_parenthesis(self, n):
	res = []
	self.create_combinations(res, n, n)
	return list(set(res))


def create_combinations(self, res, left, right, curr=""):
	if left == 0 and not right == 0:
		res.append(curr)
	else:
		if left > 0:
			self.create_combinations(res, left-1, right, curr + "(")
		if right > 0 and left < right:
			self.create_combinations(res, left, right-1, curr + ")")