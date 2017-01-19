'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Difficult: Easy

'''

def remove_duplicates(head):
	ptr = head
	while ptr:
		while ptr.next and ptr.val = ptr.next.val:
			ptr.next = ptr.next.next
		ptr = ptr.next
	return head