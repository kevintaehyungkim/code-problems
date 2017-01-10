'''
Cracking the Coding Interview
2.6: Implement a function to check if a linked list is a palindrome.
'''

def is_palindrome(head):
	if not head:
		return True
	stack = Stack()
	slow = fast = head
	while fast and fast.next:
		stack.push(slow.val)
		slow = slow.next
		fast = fast.next.next
	# odd nodes
	if fast: 
		slow = slow.next
	# even nodes
	else:
		while slow:
			if slow.val != stack.pop():
				return False
			slow = slow.next
	return True

