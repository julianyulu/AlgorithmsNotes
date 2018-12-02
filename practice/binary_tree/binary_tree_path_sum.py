# binary_tree_path_sum.py --- 
# 
# Filename: binary_tree_path_sum.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Nov  3 14:40:20 2018 (-0500)
# Version: 
# Last-Updated: Sat Nov  3 14:46:41 2018 (-0500)
#           By: yulu
#     Update #: 3
# 




class Solution:
    '''
    Definition for a binary tree node.
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    '''
    # Bottom up recursive solution
    # 60 ms, beat 46%
    def hasPathSum(self, root, sumVal = None):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """     
        res = False 
        
        if root:       
            sumVal -= root.val
            if not root.left and not root.right and sumVal == 0:
                return True          
            return self.hasPathSum(root.left, sumVal) or self.hasPathSum(root.right, sumVal)
    
        else:
            return False 
