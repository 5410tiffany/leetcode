import numpy as np
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def inorder(self, node):
        #left child
        if node.left: 
            self.inorder(node.left)
        #parent
        self.queue.append(node.val)

        #right child
        if node.right: self.inorder(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        '''
        inorder traversal: Tree由小到大排
        '''
        self.queue = []
        self.min = inf
        self.inorder(root)
        arr = np.array(self.queue)
        
        return min(arr[1:] - arr[:-1])
        
        
