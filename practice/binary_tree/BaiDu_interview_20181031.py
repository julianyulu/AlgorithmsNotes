      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

22

   [5,4,11,2]
   [5,8,4,5]
   
  [5, 4, 8, 11, None, 13, 4, 7 ,2, None]
  
  
 class Tree:
     def __init__(self, key = None, left = None, right = None):
         self.key = key
         self.left = left
         self.right = right
         
    
      
 def list2Tree(A):
     tree = Tree(A[0])
     queue = [tree.right, tree.left]
     for x in A[1:]:
         treeEntry = queue.pop()
         treeEntry.key = Tree(x)
         if not x is None: 
             queue.insert(0, treeEntry.left)
             queue.insert(0, treeEntry.right)
     return queue 
     
 def sumPath(tree, value, selected = None):
     if tree.key and not value == 0:
         selected.append(tree.key)
         sumPath(tree.left, value - tree.key, selected)
         sumPath(tree.right, value - tree.key, selected)
     elif tree.key is None and value == 0:
         print(selected)
     else:
         pass 
         
         
    a = ['ab', 'cd', 'ab']
 
def freqValue(a):
    ans = {}
    maxKeyLen = 0
    maxKey = None

    for x in a:
        try:
            ans[x] += 1
        except KeyError:
            ans[x] = 1
     
        if ans[x] > maxKeyLen:
                maxKeyLen  = ans[x]
                maxKey = x
                
                
    return maxKey 
    
       
     
     
         
   

    
     
