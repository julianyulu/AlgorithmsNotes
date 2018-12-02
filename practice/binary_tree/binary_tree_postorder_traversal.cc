// post.cc --- 
// 
// Filename: post.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 15:05:03 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 15:05:09 2018 (-0600)
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
  vector<int> postorderTraversal(TreeNode* root) {
    vector<int> res;
    if (root) postorder(root, res);
    return res;
  }
private:
  void postorder(TreeNode* root, vector<int>& v)
  {
    if(root -> left)
      postorder(root -> left, v);
    if(root -> right)
      postorder(root -> right, v);
    v.push_back(root -> val);
        
  }
};
