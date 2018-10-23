# binary_tree_inorder_traversal.py --- 
# 
# Filename: binary_tree_inorder_traversal.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Oct 21 16:39:18 2018 (-0500)
# Version: 
# Last-Updated: Sun Oct 21 16:41:38 2018 (-0500)
#           By: yulu
#     Update #: 5
#







class Solution:
    '''
    Given a binary tree, return the inorder traversal of its nodes' values.

    Definition for a binary tree node.
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    '''
    
    # Recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            temp =  [*self.inorderTraversal(root.left), root.val, *self.inorderTraversal(root.right)]
            return [x for x in temp if x]
        else:
            return []
    
    # Iterative solution
    def inorderTraversal(self, root):
        res = []
        stack = []
        while root:
            try:
                if root.right:
                    stack.append(root.right)
                stack.append(root.val)
                if root.left:
                    stack.append(root.left)
            except AttributeError:
                res.append(root)
            try:
                root = stack.pop()
            except IndexError:
                break
        return res
