# binary_tree_populate_next_right_pointer.py --- 
# 
# Filename: binary_tree_populate_next_right_pointer.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Nov  3 17:21:56 2018 (-0500)
# Version: 
# Last-Updated: Sat Nov  3 19:37:05 2018 (-0500)
#           By: yulu
#     Update #: 2
# 



class Solution:
    '''
    Given a binary tree
    struct TreeLinkNode {
    TreeLinkNode *left;
    TreeLinkNode *right;
    TreeLinkNode *next;
    }

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.
    -------------
    Definition for binary tree with next pointer.
    class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    @param root, a tree link node
    @return nothing
    '''
    # 56ms, best 36%
    def connect(self, queue):
        if not queue:
            return 
        if hasattr(queue, '__iter__'):
            pass
        else:
            queue = [queue]
            
        currQueue = []
        if queue:
            start = queue.pop()

            while queue:                
                if start.left:
                    currQueue.insert(0, start.left)
                if start.right:
                    currQueue.insert(0, start.right)
                start.next = queue.pop()
                start = start.next
            start.next = None
            if start.left:
                currQueue.insert(0, start.left)
            if start.right:
                currQueue.insert(0, start.right)
            self.connect(currQueue)
