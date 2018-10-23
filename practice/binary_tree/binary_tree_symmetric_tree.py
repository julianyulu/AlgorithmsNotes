# binary_tree_symmetric_tree.py --- 
# 
# Filename: binary_tree_symmetric_tree.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Tue Oct 23 01:09:35 2018 (-0500)
# Version: 
# Last-Updated: Tue Oct 23 01:10:34 2018 (-0500)
#           By: yulu
#     Update #: 2
# 


class Solution:
    '''
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
     
    Definition for a binary tree node.
    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    '''

    # Itterative solution
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        currentLayer = []
        while queue:
            currentLayer = queue
            queue = []
            while currentLayer:
                front = currentLayer.pop()
                try:
                    back = currentLayer.pop()
                except IndexError:
                    back = front
                
                if front and back: # if both front back are not None
                    if back.val == front.val: # Prepare next layer check
                        queue.insert(0, front.left)
                        queue.insert(0, back.right)
                        queue.insert(0, front.right)
                        queue.insert(0, back.left)

                    else:
                        return False
                elif front: # one None the other not: definite no symmetric
                    return False
                elif back:
                    return False
                else: # both None, symmetric 
                    pass
        return True
