"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # index corresponds to the node , the actual list is its neighbords
        oldToNew = {}

        def clone(node): # dfs
            if node in oldToNew:
                return oldToNew[node] 
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None
        # Runtime: O(V + E), because we made a clone of every node and its edges

