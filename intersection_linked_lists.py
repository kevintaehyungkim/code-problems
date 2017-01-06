'''
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

'''

def find_intersect(head1, head2):
	pointA = head1
	pointB = head2
	switch = 1
	while pointA and pointB:
		if pointA == pointB:
			return pointA
		elif switch % 2:
			pointA = pointA.next
		else:
			pointB = pointB.next
		switch = 1 - switch
	return None

