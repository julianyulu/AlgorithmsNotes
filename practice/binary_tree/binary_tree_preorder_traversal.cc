// preorderTraversal.cc --- 
// 
// Filename: preorderTraversal.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 14:38:19 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 14:38:46 2018 (-0600)
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
  vector<int> preorderTraversal(TreeNode* root) {
    vector<int> res;
    if(root) preTraversal(root, res);
    return res;
  }   
  void preTraversal(TreeNode* root, vector<int>& v){
    v.push_back(root -> val);
    if(root -> left) preTraversal(root -> left, v);
    if(root -> right) preTraversal(root -> right, v);
  }
};
