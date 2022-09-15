# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(left_val,right_val):
            if left_val == None and right_val == None:
                return True
        
            elif (left_val != None and right_val != None) and (left_val.val == right_val.val):
                return check(left_val.left,right_val.right) and check(left_val.right,right_val.left)
        
            else:
                return False
        
        return check(root.left,root.right)
        