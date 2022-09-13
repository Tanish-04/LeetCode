# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    Sum = 0
    
    def getHeight(self,root):
        
        if root == None:
            return 0
        return (1 + max(self.getHeight(root.left), self.getHeight(root.right))) 
    
    def getSum(self,root, height):
        
        if root == None:
            return self.Sum
        
        if height == 0:
            self.Sum = self.Sum + root.val
            
        self.getSum(root.left, height - 1)
        self.getSum(root.right, height - 1)
        
        return self.Sum
        
        
    def deepestLeavesSum(self, root):
        height = self.getHeight(root)
        self.getSum(root, height - 1)
        return self.Sum
        
        
        