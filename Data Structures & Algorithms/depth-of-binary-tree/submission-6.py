# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        
        height = 0
        
        
        while queue: # is not empty
            for i in range(len(queue)):
                node = queue.popleft() # pops out the root 
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            height += 1
        return height
            







        
        

