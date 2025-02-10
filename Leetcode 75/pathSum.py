'''
437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum_count = defaultdict(int)
        sum_count[0] = 1

        def dfs(root, current_sum):
            if not root:
                return 0
            
            current_sum += root.val
            paths = sum_count[current_sum - targetSum]  
           
            sum_count[current_sum] += 1
            
            paths += dfs(root.left, current_sum)
            paths += dfs(root.right, current_sum)
            
            sum_count[current_sum] -= 1
            
            return paths
        
        return dfs(root, 0)