# binary_tree_preorder_traversal.py --- 
# 
# Filename: binary_tree_preorder_traversal.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Oct 21 16:25:07 2018 (-0500)
# Version: 
# Last-Updated: Sun Oct 21 16:42:04 2018 (-0500)
#           By: yulu
#     Update #: 6
# 

class Solution:
    '''
    Given a binary tree, return the preorder traversal of its nodes' values.

    Definition for a binary tree node.
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    '''
    
    #Recursive solution
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:     
            return []
        else:
            return [root.val, *self.preorderTraversal(root.left), *self.preorderTraversal(root.right)]
     
    #Iterative solution
    def preorderTraversal(self, root):
        res = []
        stack = []
        while root:
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            try:
                root = stack.pop()
            except IndexError:
                break
            
        return res
         
