'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Difficulty: Easy

Solution notes:
O(n) time
O(1) space
'''

def add_two_numbers(head1, head2):
	result = output = ListNode(0)
	while head1 or head2:
		val1 = val2 = 0
		if head1:
			val1 = head1.val
		if head2:
			val2 = head2.val
		output.val = output.val + val1 + val2
		if output.val > 10:
			output.next = ListNode(1)
			output.val -= 10
		else:
			output.next = ListNode(0)
		output = output.next
	return result






