// binary_tree_lowest_common_ancestor.cc --- 
// 
// Filename: binary_tree_lowest_common_ancestor.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Sat Dec  1 20:32:43 2018 (-0600)
// Version: 
// Last-Updated: Sat Dec  1 20:32:50 2018 (-0600)
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
class Solution {
public:
  // recursive solution
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    TreeNode* left;
    TreeNode* right;
    if(!root) return nullptr; 
    if(root -> val == p -> val || root -> val == q -> val) return root;      
    else{
      left = lowestCommonAncestor(root -> left, p, q);
      right = lowestCommonAncestor(root -> right, p, q);
      if(left && right) return root;
      if(left) return left;
      if(right) return right;
    }
    return nullptr;
  }
        
};
