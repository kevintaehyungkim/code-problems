'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Difficult: Easy

This code if duplicates don't have to be adjacent:

def remove_duplicates(head):
	ptr = head
	arr = []
	while ptr:
		if ptr.val in arr:
			ptr.prev.next = ptr.next
			ptr.next.prev = ptr.prev
		else:
			arr.append(ptr.val)
	return head
'''

def remove_duplicates(head):
	ptr = head
	while ptr:
		if ptr.next and ptr.val = ptr.next.val:
			ptr.next = ptr.next.next
		ptr = ptr.next
	return head