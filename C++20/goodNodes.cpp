/*
1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Time: O(N)
Space: O(N)
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    public:
        int dfs(TreeNode* node, int max_so_far) {
            if (!node) return 0;
    
            int good = (node -> val >= max_so_far) ? 1 : 0;
            max_so_far = max(max_so_far, node->val);
            
            return good + dfs(node->left, max_so_far) + dfs(node->right, max_so_far);
        }
    
        int goodNodes(TreeNode* root) {
            return dfs(root, root->val);
        }
    };