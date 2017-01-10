'''
Cracking the Coding Interview
4.10: T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1. 
A tree T2 is a subtree of T1 if there exists node n in T1 such that the subtree of n is identical
to T2. That is, if you cut off the tree at node n, the two trees would be identical.
'''

def binary_subtree(t1, t2):
	if not t2:
		return False
	return contains_tree(t1,t2)


def contains_tree(r1, r2):
	if not r1:
		return False
	elif r1.val == r2.val and same_tree(r1,r2):
		return True
	else:
		return binary_subtree(r1.left, r2) or binary_subtree(r1.right, r2)


def same_tree(node1, node2):
	if not node1 and not node2:
		return True
	elif node1 and node2 and node1.val == node2.val:
		return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)
	else:
		return False