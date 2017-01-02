'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Difficulty: Medium

'''
#recursive solution
def inorder_traversal(root):
	if root == null:
		return
	inorder_traveral(root.left)
	append(root)
	inorder_traversal(root.right)


#iterative solution
def inorder_traversal(root):
	answer = []
	stack = []
	while root or stack:
		if root:
			stack.append(root)
			root = root.left
		else:
			latest_node = stack.pop()
			answer.add(latest_node)
			root = latest_node.right
	return answer


