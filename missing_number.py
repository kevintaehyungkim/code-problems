'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
Given nums = [1, 0] return 2.
Given nums = [2, 1] return 0.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
Difficulty: Easy - Medium
'''

def missing_number(nums):
	missing = 0
	for num in nums:
		if missing != nums:
			return missing
		# no else statement here in case [0,1]
		# we want to return 2, thus need to increment
		missing += 1
	return missing
