# maxinium_depth_of_binary_tree.py --- 
# 
# Filename: maxinium_depth_of_binary_tree.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Tue Oct 23 00:20:04 2018 (-0500)
# Version: 
# Last-Updated: Tue Oct 23 00:21:37 2018 (-0500)
#           By: yulu
#     Update #: 2
# 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Top down recursion and bottom up recursion

    Definition for a binary tree node.
    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    '''
    # Top-down solution 52 ms
    ans = 0 
    def maxDepth(self, root, depth = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.maxDepth(root.left, depth + 1)
            self.maxDepth(root.right, depth + 1)
        else:
            self.ans = max(self.ans, depth)
        return self.ans
    
    # Bottom up solution 84 ms
    def maxDepth(self, root):
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1
        else:
            return 0 
