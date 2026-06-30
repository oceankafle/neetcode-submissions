# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        lower, upper = float("-infinity"), float("infinity") # initially -inf and inf

        def dfs(node, lower, upper):
            if not node:
                return True
            
            print("This is the node we're on:",node.val)
            print("This is the lower bound:", lower)
            print("This is the upper bound:", upper)

            
            if lower < node.val < upper: # valid so far
                if dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper):
                    return True
                else:
                    return False

        
        if dfs(root, lower, upper):
            return True
        else:
            return False
