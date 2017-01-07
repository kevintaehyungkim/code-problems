'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Difficult: Medium
'''

def odd_even(head):
	if not head:
		return None
	if not head.next:
		return head
	odd = odd_start = head
	even = even_start = head.next
	while odd and even:
		if even.next:
			odd.next = even.next
			odd = odd.next
			even.next = odd.next
			even = even.next
		else:
			even = even.next
	odd.next = even_start
	return odd

