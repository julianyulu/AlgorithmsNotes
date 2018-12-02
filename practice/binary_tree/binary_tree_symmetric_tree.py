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
# Last-Updated: Sat Oct 27 18:44:05 2018 (-0500)
#           By: yulu
#     Update #: 5
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
    # an ugly iterative solution 56 ms, 30%
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
                elif front or back: # one None the other not: definitely not symmetric
                    return False
                else: # both None, symmetric 
                    pass
        return True

        # recursive solution, very slow, 1.8s, beat 0%
        def isSymmetric(self, root):
        
            root = root if hasattr(root, '__iter__') else [root]
            length = len(root) // 2          
            queue = []
            for leftIdx in range(length):
                rightIdx =  len(root) - leftIdx - 1
                val1 = root[leftIdx].val if root[leftIdx] else root[leftIdx]
                val2 = root[rightIdx].val if root[rightIdx] else root[rightIdx]
                
                if not val1 == val2:
                    print(val1, val2)
                    return False  
           
            queue = []
            for x in root:
                queue.append(x.left if x else None)
                queue.append(x.right if x else None)
                
            if any(queue):
                return self.isSymmetric(queue)
            else:
                return True
                    
        # a much simpler iterative solution with stack 56 ms beat 30%
        def isSymmetric(self, root):
            # add to stack the pairs what to compare
            # no need to go layer by layer in the tree
            if root:
                stack = [root.left, root.right]
            else:
                return True
            while stack:
                val1 = stack.pop()
                val2 = stack.pop()
                if val1 and val2 and val1.val == val2.val: # both are not none 
                    stack[len(stack):] = [val1.left, val2.right, val1.right, val2.left]
                elif (not val1) and (not val2): # both are none 
                    continue 
                else:
                    return False
            return True
           
            
