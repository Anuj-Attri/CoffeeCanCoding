'''
1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

'''
Gist:

'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            count = 1 if node.val >= max_so_far else 0
            new_max = max(node.val, max_so_far)

            return dfs(node.left, new_max) + dfs(node.right, new_max) + count

        return dfs(root, root.val)