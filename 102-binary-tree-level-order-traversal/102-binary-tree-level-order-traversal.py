# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return None
        # Keeping tracks of levels
        treeLevel = []
        
        def helper(node,level):
            
            if len(treeLevel) == level:
                treeLevel.append([])
            
            treeLevel[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
            return treeLevel
        
        
        return helper(root,0)