// symmetic.cc --- 
// 
// Filename: symmetic.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 16:39:17 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 16:39:25 2018 (-0600)
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
  bool isSymmetric(TreeNode* root) {
    if(root)
      return compareLeftRight(root -> left, root -> right);
    else
      return true;
  }
  bool compareLeftRight(TreeNode* leftnode, TreeNode* rightnode)
  {
    if(leftnode && rightnode)
      {
	if (leftnode -> val != rightnode -> val) return false;

	if(compareLeftRight(leftnode -> left, rightnode -> right) &&
	   compareLeftRight(leftnode -> right, rightnode -> left) )
	  return true;
	return false;
      }
    else if (!leftnode && !rightnode)
      return true;
    else
      return false;
  }
};
