'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

Difficulty: Easy
'''

def array_intersection(arr1, arr2):
	return list(set([i for i in arr1 if i in arr2]))