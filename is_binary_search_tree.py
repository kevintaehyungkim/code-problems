'''
Cracking the Coding Interview
4.5: Implement a function to check if a binary tree is a binary search tree.

We can't simply recurse through tree's children and check for left <= current < right
because they'll be cases such as:
      20 
   10    30
      25
where 25 is indeed greater than 10, but is not in its right place. 
Thus implement in-order search.
'''
# in-order traversal
last_val = None
def check_bst(node):
	if not node:
		return True
	# recurse left
	if not check_bst(node.left):
		return False
	# check current node
	if last_val and node.val <= last_val:
		return False
	last_val = node.val
	# recurse right
	if not check_bst(node.right):
		return False
	return True
