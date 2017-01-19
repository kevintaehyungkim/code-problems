'''
Given a binary tree, return the longest distance between any two nodes.

Initial Thoughts:
use recursion
if no node, return 0
use helper method to calculate max heights from root.left and root.right
add the two together to create longest distance
'''

def longest_path(root):
	if not root:
		return 0
	return max_height(root.left) + max_height(root.right)

# this method returns height of given root
def max_height(t, sum):
	if not t:
		return 0
	return max(1 + max_height(t.left), 1 + max_height(t.right))