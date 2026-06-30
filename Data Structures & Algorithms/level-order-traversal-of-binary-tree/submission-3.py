# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS --> Queue and pop for each level 
        # create a new list at each level 

        if not root:
            return []
        
        q = deque()
        q.append(root) # q = [2, 3]
        final = []
        
        while q:
            level = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            final.append(level)

        return final

            













        