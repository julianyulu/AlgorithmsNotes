// sum.cc --- 
// 
// Filename: sum.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 17:23:03 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 17:23:11 2018 (-0600)
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
  bool hasPathSum(TreeNode* root, int sum) {
    if(root)
      return checkPathSum(root, sum);
    else
      return false;
  }
    
private:
  bool checkPathSum(TreeNode* root, int sum)
  {   bool res = false;

    if (root -> left)
      res = res || checkPathSum(root -> left, sum - (root -> val));
    if (root -> right)
      res = res || checkPathSum(root -> right, sum  - (root -> val));

    if (!root -> left && !root -> right && root -> val == sum)
      res = true;
    return res;
        
  }
};
