# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(node, lower, upper):
            if not node:
                return True
            
            if lower < node.val < upper: # valid so far
                if dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper):
                    return True
                else:
                    return False

        
        if dfs(root, float("-infinity"), float("infinity")):
            return True
        else:
            return False
