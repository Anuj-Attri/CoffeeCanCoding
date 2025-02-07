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

