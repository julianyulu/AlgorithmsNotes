// depth.cc --- 
// 
// Filename: depth.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 16:14:16 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 16:14:42 2018 (-0600)
//           By: yulu
//     Update #: 1
// 

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

Top-down solution 
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int answer = 0;
        if (root)
            getMaxDepth(root, answer, 1);
        return answer;
    }
private:
    void getMaxDepth(TreeNode* root, int& answer, int depth)
    {   
        if (root -> left)
            getMaxDepth(root -> left, answer, depth + 1);
        if (root -> right)
            getMaxDepth(root -> right, answer, depth + 1);
        if (!root -> left && !root -> right)
            answer = max(answer, depth);
    }

};

Bottom solution
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root)
            return 0;
        int leftmax = maxDepth(root -> left);
        int rightmax = maxDepth(root -> right);
        return max(leftmax + 1, rightmax + 1);
            
    }
};
