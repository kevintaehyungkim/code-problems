'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Difficult: Easy

Solution Notes:
1. Use the property of sets (unique). 
2. Alternatively, use a hash map to keep track of how many times elements appear.

Time: O(n)
Space: O(1)
'''

# one line Solution
def contains_duplicates(nums):
	return len(nums) > len(set(nums))

# hash_map Solution
def contains_duplicates(nums):
	dup_map = {}
	for num in nums:
		if num in dup_map:
			return True
		else:
			dup_map[num] = 1
	return False
