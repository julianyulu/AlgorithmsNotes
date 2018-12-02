// inorder.cc --- 
// 
// Filename: inorder.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 15:01:03 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 15:01:10 2018 (-0600)
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
  vector<int> inorderTraversal(TreeNode* root) {
    vector<int> res;
    if (root) inorder(root, res);
    return res;
        
  }
    
private:  
  void inorder(TreeNode* root, vector<int>& v)
  {
    if (root -> left)
      inorder(root -> left, v);
    v.push_back(root -> val);
    if (root -> right)
      inorder(root -> right, v);
  }
};
