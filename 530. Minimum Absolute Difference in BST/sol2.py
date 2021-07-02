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
        self.min = min(abs(node.val - self.prev), self.min)
        self.prev = node.val
        
        #right child
        if node.right: self.inorder(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        '''
        inorder traversal: Tree由小到大排
        '''
        self.min = inf
        self.prev = inf
        self.inorder(root)
        
        
        return self.min
        
        
