'''
872. Leaf-Similar Trees
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

'''
Gist:

Using recursion, find traverse the trees to find the leaf nodes in both root1 and root2, and append them to an array 'leaves'.
Comparing the two outputs of 'getleaves' will return if the two trees are leaf similar or not.

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getleaves(root):
            leaves = []

            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    leaves.append(node.val)

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves
        return getleaves(root1) == getleaves(root2)