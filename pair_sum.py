# -*- coding: utf-8 -*-
'''
Example problem from Youtube video: "How to: Work at Google — Example Coding/Engineering Interview"

If two numbers in array equals given sum, return true

ex: [1,2,3,9], sum = 8 -> false
ex: [1,2,4,4], sum = 8 -> true

Time: O(n)
Space: O(1)

'''

def has_pair_sum(nums, sum):
	low = 0
	high = len(nums) - 1
	while (low != high):
		if nums[low] + nums[high] > sum:
			high -= 1
		elif nums[low] + nums[high] < sum:
			low += 1
		else:
			return True
	return False
