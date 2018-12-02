# binary_tree_inorder_posterorder_traversal.py --- 
# 
# Filename: binary_tree_inorder_posterorder_traversal.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Nov  3 16:16:59 2018 (-0500)
# Version: 
# Last-Updated: Sat Nov  3 16:17:48 2018 (-0500)
#           By: yulu
#     Update #: 1
# 



class Solution:
    """
    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.

    -----
    I took solution from: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/discuss/34814/A-Python-recursive-solution
    
    Definition for a binary tree node.
    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    """
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None 
        
        tree = TreeNode(postorder.pop())
        rootidx = inorder.index(tree.val)
        tree.right = self.buildTree(inorder[rootidx + 1:], postorder)
        tree.left = self.buildTree(inorder[:rootidx], postorder)
        return tree
