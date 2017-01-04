'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

For example:
Given nums = [1, 2, 1, 3, 2, 5]
return [3, 5]

Difficulty: Medium
'''

def single_numbers(nums):
	seen = {}
	for num in nums:
		if num in seen.keys():
			del seen[num]
		else:
			seen[num] = 1
	return seen.keys()


if __name__ == '__main__':
	print single_numbers([1, 2, 1, 3, 2, 5])