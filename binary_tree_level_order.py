'''
 How do you print out the nodes of a binary tree in level-order?  
 
     1
   2    3
 4  5  6  7
   
   123
   
   Queue: 1
   Queue: 2,3  
'''

def level_order(root):
	q = Queue()
	q.enqueue(root)
	while q.size() > 0:
		node = q.dequeue
		print node.val
		if node.left:
			q.enqueue(node.left)
		if node.right:
			q.enqueue(node.right)
	return

