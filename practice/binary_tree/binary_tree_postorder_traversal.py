# binary_tree_postorder_traversal.py --- 
# 
# Filename: binary_tree_postorder_traversal.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Oct 21 16:49:06 2018 (-0500)
# Version: 
# Last-Updated: Sun Oct 21 16:49:57 2018 (-0500)
#           By: yulu
#     Update #: 1
# 


class Solution:
    '''
    Given a binary tree, return the postorder traversal of its nodes' values.
    Follow up: Recursive solution is trivial, could you do it iteratively?

    Definition for a binary tree node.
    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    '''
    # Recursive solution 
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            temp = [*self.postorderTraversal(root.left), *self.postorderTraversal(root.right), root.val]
            return [x for x in temp if x]
        else:
            return []
    
    # Iterative solution
    def postorderTraversal(self, root):
        res = []
        stack = []
        while root:
            try: 
                stack.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
            except AttributeError:
                res.append(root)
            
            try:
                root = stack.pop()
            except IndexError:
                break
        return res
