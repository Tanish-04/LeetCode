# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        if root == None:
            return False
        return self.helper(root, targetSum)
    
    def helper(self, root, Sum):
        if root == None:
            return False
        
        Sum = Sum - root.val
        
        if (root.left == None and root.right == None and Sum == 0): return True
        
        return self.helper(root.left, Sum) or self.helper(root.right, Sum)
        