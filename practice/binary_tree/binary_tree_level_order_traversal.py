# binary_tree_level_order_traversal.py --- 
# 
# Filename: binary_tree_level_order_traversal.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Mon Oct 22 00:29:14 2018 (-0500)
# Version: 
# Last-Updated: Mon Oct 22 00:30:12 2018 (-0500)
#           By: yulu
#     Update #: 2
# 


class Solution:
    '''
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    Definition for a binary tree node.
    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    '''
    
    # NOT an efficient solution, only beats 10% submissions 
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        nextQueue = [root] if root else []
        while nextQueue:
            queue = nextQueue
            nextQueue = []
            currLayer = []
            while queue:
                curr = queue.pop()
                currLayer.append(curr.val)
                if curr.left:
                    nextQueue.insert(0, curr.left)
                if curr.right:
                    nextQueue.insert(0, curr.right)
            res.append(currLayer)        
        return res 
            
        
