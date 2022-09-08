# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        newList = []

        if root == None:
            return

        if root.left:
            newList += (self.postorderTraversal(root.left))
            
        if root.right:
            newList += (self.postorderTraversal(root.right))

        newList.append(root.val)

        return newList
        
            
        