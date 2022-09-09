# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root):
        
        l,r = 0,0
        
        if root.left:
            l += self.dfs(root.left)
        
        if root.right:
            r += self.dfs(root.right)
            
        if abs(l-r) > 1:
            self.answer = False
        
        return max(l,r) + 1
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        self.answer = True
        
        self.dfs(root)
        
        return self.answer
        