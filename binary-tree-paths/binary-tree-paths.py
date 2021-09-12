# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def tree_paths(self,node, path, lst):
            if not node: 
                return lst
        
            if not node.left and not node.right: 
                lst.append(path)
                return lst

            if node.left: 
                self.tree_paths(node.left, path+f"->{node.left.val}",lst)

            if node.right: 
                self.tree_paths(node.right, path+f"->{node.right.val}",lst)

            return lst 

    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        if not root:       
            return []

        return self.tree_paths(root, f"{root.val}",[])  
                       
        
        
                
    