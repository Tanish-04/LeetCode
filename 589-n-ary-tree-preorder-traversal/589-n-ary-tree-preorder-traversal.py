"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # Preorder
        # 1,3,5,6,2,4
        # 1,2,3,6,7,11,14,4,8,12,5,9,13,10
        
        
        if root is None:
            return []
        
        def helper(root):
            result.append(root.val)
            for child in root.children:
                helper(child)
            
        
        result = []
        helper(root)
        return result
            