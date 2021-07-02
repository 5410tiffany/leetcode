# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nodeheight(self, node):
        if node is None: return 0
        else:
            lh = self.nodeheight(node.left)
            rh = self.nodeheight(node.right)
            
            # update diameter, lh + rh is the diamter that returns @node
            self.diameter = max(self.diameter, lh + rh)
            return max(lh, rh) + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
        trap: diameter MAY NOT pass the root
        '''
        self.diameter = 0
        self.nodeheight(root)
        return self.diameter
        
