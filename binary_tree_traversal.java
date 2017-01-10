/* 
Code for following binary tree traversals: 
	in-order
	pre-order
	post-order
*/

void inOrder(TreeNode node){
	if (node != null){
		inOrder(node.left)
		visit(node)
		inOrder(node.right)
	}
}

void preOrder(TreeNode node){
	if (node != null){
		visit(node)
		preOrder(node)
		postOrder(node)
	}
}

void postOrder(TreeNode node){
	if (node != null){
		postOrder(node.left)
		postOrder(node.right)
		visit(node)
	}
}