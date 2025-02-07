'''
1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

'''
Gist:
Solving this problem uising an explicit stack will result in a more efficient memory management, and reduces Python's recursion overhead.
The time and space complexities remain the same, but the program proves to be much more memory efficient and scalable.

Time: O(N)
Space: O(H)
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        good_nodes = 0

        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good_nodes += 1

            new_max = max(max_so_far, node.val)

            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))

        return good_nodes