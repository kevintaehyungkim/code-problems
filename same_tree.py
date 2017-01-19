'''
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Difficult: Easy

Solution Notes:
O(n) time
O(1) space
'''

def same_tree(t1, t2):
	if not t1 and not t2:
		return True
	elif t1 and t2 and t1.val == t2.val:
		return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)
	else:
		return False