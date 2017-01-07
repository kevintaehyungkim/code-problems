'''
Given a linked list, determine if it has a cycle in it.
'''


def has_cycle(head):
	slow = fast = head
	while fast:
		slow = slow.next
		if fast.next:
			fast = fast.next.next
		else: 
			return False
		if slow is fast:
			return True
	return False
