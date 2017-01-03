# -*- coding: utf-8 -*-
'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
[1], 1 → 0

'''

def search_insert(nums, val):
	if len(nums) == 0:
		return 0
	mid = len(nums)/2
	if val <= nums[mid]:
		return search_insert(nums[0:mid],val)
	elif val > nums[mid]:
		return mid + 1 + search_insert(nums[mid+1:len(nums)],val)



if __name__ == '__main__':
  print search_insert([1,3,5,6],2)





