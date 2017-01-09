'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 

Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Difficulty: Easy

def happy_number(num):
	prev = set()
	while True:
		print(num)
		if num in prev:
			return False
		prev.add(num)
		num = sum([int(k)**2 for k in str(num)])
		if num == 1:
			return True
	return False

The above solution can take a lot of space depending on how many iterations
of the while loop it takes to end up at 1. Thus, the solution below saves space
using Floyd's cycle-detection algorithm.

'''

def happy_number(num):
	slow = digit_sum(num)
	fast = digit_sum(slow)
	while True:
		if slow == 1 or fast == 1:
			return True
		else:
			slow = digit_sum(slow)
			fast = digit_sum(digit_sum(fast))
		if slow == fast:
			return False


def digit_sum(k):
	return sum([int(i)**2 for i in str(k)])


if __name__ == '__main__':
  print happy_number(20)