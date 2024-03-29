# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        
        # preorder traversal    1,2,4,3
        # postorder traversal   4,2,3,1
        # inorder traversal     4,2,1,3

        if root == None:
            return ""
        
        
        # when left and right doesn't exist
        if root.left == None and root.right == None:
            return str(root.val)
        
        # left exist but right doesn't
        if root.right == None:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        
        # when left and right exist
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
        
        
        
        