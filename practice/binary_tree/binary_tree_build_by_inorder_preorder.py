# binary_tree_build_by_inorder_preorder.py --- 
# 
# Filename: binary_tree_build_by_inorder_preorder.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Nov  3 16:27:15 2018 (-0500)
# Version: 
# Last-Updated: Sat Nov  3 16:28:15 2018 (-0500)
#           By: yulu
#     Update #: 1
# 


class Solution:
    '''
    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.
    ---------

    Definition for a binary tree node.
    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    '''
    # Runtime 228ms, beat 46%
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None 
        
        root = preorder[0]
        tree = TreeNode(root)
        preorder.remove(root)
        idx = inorder.index(root)
        
        tree.left = self.buildTree(preorder, inorder[:idx])
        tree.right = self.buildTree(preorder, inorder[idx + 1:]) 
        
        return tree
