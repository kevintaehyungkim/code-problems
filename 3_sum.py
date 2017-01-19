'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Difficult: Medium

Solution Notes:
Sort list, then use 2 pointers to cover every combination. See 3_sum_closest for more explanation.

O(n^2) time
O(1) space
'''
# if three elements equal 0
def triple_sum(nums):
	res = []
	sorted_nums = sorted(nums)
	for low in xrange(len(sorted_nums)-2):
		med = low+1
		high = len(sorted_nums)-1
		while med < high:
			temp_list = [sorted_nums[low], sorted_nums[med], sorted_nums[high]]
			s = sum(temp_list)
			if s < 0:
				med+=1
			elif s > 0:
				high-=1
			else:
				if temp_list not in res:
					res.append(temp_list)
				med+=1
	return res


# if three elements equal given k
def triple_sum(nums, k):
	res = []
	nums.sort()
	for low in range(0, len(nums)-2):
		mid = low + 1
		high = len(nums) - 1
		while mid < high:
			temp_list = [nums[low], nums[mid], nums[high]]
			s = sum(temp_list)
			if s > k:
				high -= 1
			elif s < k:
				mid += 1
			else:
				if temp_list not in res:
					res.append(temp_list)
				mid += 1
	return res



if __name__ == '__main__':
	print triple_sum([-1, 0, 1, 2, -1, -4])






	
