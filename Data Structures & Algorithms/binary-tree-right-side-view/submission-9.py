# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS level order traversal
        if not root:
            return []
        
        q = deque([root])
        final = []

        while q: # q = [2, 3]
            right_side = None
            for _ in range(len(q)):
                node = q.popleft() # pops the 1

                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            # we hit the end of our "level", meaning rightSide holds the rightmost val
            if right_side:
                final.append(right_side.val) # 
        return final









