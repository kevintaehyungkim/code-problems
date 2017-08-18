'''
Cracking the Coding Interview
4.4: Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never 
differ by more than one.
'''

def is_balanced(node):
	if not node:
		return True
	if get_height(node.left) == get_height(node.right):
		return is_balanced(root.left) and is_balanced(root.right)
	else:
		return False

def get_height(node):
	if not node:
		return 0
	return max(1+get_height(node.left), 1+get_height(node.right))
