'''
Cracking the Coding Interview
8.1: A child is running up a staircase with n steps and can hop either 
1 step, 2 step, or 3 steps at a time. Implement a method to count how many ways
the child can run up the stairs.

# Recursive = O(3^n) so too slow
def triple_step(k):
	if k < 0:
		return 0
	elif k == 0:
		return 1
	else:
		return triple_step(k-3) + triple_step(k-2) + triple_step(k-1)
'''

# Memoization = O(1.6^n)
def triple_step(k):
	memo_arr = [None]*(k+1)
	return count_ways(k, memo_arr)

def count_ways(n, memo_arr):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif memo_arr[n]:
		return memo_arr[n]
	else:
		memo_arr[n] = count_ways(n-1, memo_arr) + count_ways(n-2, memo_arr) + count_ways(n-3, memo_arr)
		return memo_arr[n]


if __name__ == '__main__':
  print triple_step(900)