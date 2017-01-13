'''
Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

Difficult: Easy
'''

def sum_left(self, node, left=False):
	if node:
		if not node.left and not node.right and left:
			return node.val
		else:
			return self.sum_left(node.left, True) + self.sum_left(node.right, False)
	else:
		return 0