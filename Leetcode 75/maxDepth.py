'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

'''
Gist:
Given the definition of tree node, we can recursively call the function to perform depth first search.
The base case is when the root is 0, signifying a leaf node. 
The maximum depth of any branch in a binary tree is the max(left child, right child).
The child becomes the root, to check the depth of the branches recursively. 
Recursion stops when an empty tree is found at the root.
Adding 1 to the recursion adds the depth of the previous parent and moves on to the branch.

Time: O(N)
Space: O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))