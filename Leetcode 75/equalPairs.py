'''
2352. Equal Row and Column Pairs
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''
'''
Gist:
Convert the rows of the grid to a tuple and count their frequencies.
Iterate over the transposed grid to obtain columns.
Increment the count when the column is found in the Counter dict.

Time: O(N+M)
Space: O(N+M)

'''
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        count = 0

        for col in zip(*grid):
            count += rows[col]

        return count