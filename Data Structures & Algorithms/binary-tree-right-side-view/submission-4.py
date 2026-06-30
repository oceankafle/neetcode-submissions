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
        
        q = deque()
        q.append(root)
        final = []

        while q: # q = [2, 3]
            level = []
            for _ in range(len(q)):
                node = q.popleft() # pops the 1 
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            final.append(level[-1])

        return final









