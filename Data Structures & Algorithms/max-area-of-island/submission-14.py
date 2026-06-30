class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set() # keep track of which cells we've seen, to prevent duplicate processing

        def dfs(r, c):
            if (r not in range(rows) or # not a 1
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] == 0):
                    return 0 # don't even calculate maxArea because invalid spot
            # valid cell
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea 