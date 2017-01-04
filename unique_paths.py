'''
A robot is located at the top-left corner of a m x n grid (marked 'R' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'F' in the diagram below).

How many possible unique paths are there?
[R] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [F]
(Above is a 3 x 7 grid. How many possible unique paths are there?)

Note: m and n will be at most 100.

Difficulty: Medium
'''

def uniquePaths(m, n):
  grid = [[1 for i in xrange(n)] for j in xrange(m)]
  for i in xrange(1, n):
    for j in xrange(1, m):
      grid[i][j] = grid[i-1][j] + grid[i][j-1]
  return grid[m-1][n-1]


if __name__ == '__main__':
  print uniquePaths(7,3)