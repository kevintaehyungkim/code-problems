'''
Given a sorted array with duplicates and a number, find the range in the
form of (startIndex, endIndex) of that number. For example,

find_range({0 2 3 3 3 10 10}, 3) should return (2,4).
find_range({0 2 3 3 3 10 10}, 6) should return (-1,-1).
The array and the number of duplicates can be large.
'''

# idea: binary search to find start index, 
# then iterate through arr from that index until the end
# if number not found, return (-1, -1)

def start_end(arr, num):
	
