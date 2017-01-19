'''
Amazon Coding Challenge 2016-2017, Round 2
Given a string of parentheses, return the number of pairs if balanced. 
If not return -1
'''

def balance_parentheses(str):
	if no str:
		return -1
	stack = Stack()
	count = 0
	for s in str:
		if s == '(':
			stack.push(s)
			count += 1
		elif s == ')':
			if len(stack) > 0:
				stack.pop()
			else:
				return -1
	if len(stack) == 0:
		return count
	return -1
