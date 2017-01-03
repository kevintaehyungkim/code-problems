'''
Given a set of distinct integers, nums, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Difficulty: Medium
Solution notes:
recursion
O(n^2) time
O(n) space
'''

def subsets(nums):
	arr = []
	for i in range(0, len(nums)-1):
		temp = []
		for j in range (i+1, len(nums)+1):
			arr.append(nums[i:j])
	arr.append([])
	return arr

if __name__ == '__main__':
  print subsets([1,2,3])
  
