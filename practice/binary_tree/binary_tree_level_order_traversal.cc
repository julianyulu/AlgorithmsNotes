// level.cc --- 
// 
// Filename: level.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Thu Nov 22 15:33:55 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 15:34:05 2018 (-0600)
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
  vector<vector<int>> levelOrder(TreeNode* root) {
    queue<TreeNode*> nodeQueue;
    queue<TreeNode*> nextQueue;
    vector<vector<int>> res;
    vector<int> levelRes;
    TreeNode* node;
    if(root) nodeQueue.push(root);
        
    while(!nodeQueue.empty() || !nextQueue.empty())
      {   
	if(nodeQueue.empty()) // move to next level
	  {
	    nodeQueue = nextQueue;
	    nextQueue = {};
	    res.push_back(levelRes);
	    levelRes = {};
	  }
	node = nodeQueue.front();
	nodeQueue.pop();
	//cout << node -> val << endl;
	levelRes.push_back(node -> val);
	if (node -> left) nextQueue.push(node -> left);
	if (node -> right) nextQueue.push(node -> right);
      }
    if(!levelRes.empty()) res.push_back(levelRes); // add last level result 
    return res;
        
  }
};

        
