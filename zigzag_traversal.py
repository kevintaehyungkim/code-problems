'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree:
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

Difficulty: Medium

Solution notes:
O(n) time
O(n) space
'''

def zigzag_traversal(root):
	if root == None:
		return []

	res = []
	level = 0
	root_stack = [root]
	res.append(root_stack)

	while (root_stack):
		level += 1
		temp_stack = root_stack
		root_stack = []
		for root in temp_stack:
			if root.left:
				root_stack.append(root.left)
			if root.right:
				root_stack.append(root.right)
		if level % 2 and root_stack: 		# root stack is odd level (reverse)
			res.append(root_stack[::-1])
		elif (!level % 2) and root_stack:	# root stack is even level (regular)
			res.append(root_stack)
	return res




