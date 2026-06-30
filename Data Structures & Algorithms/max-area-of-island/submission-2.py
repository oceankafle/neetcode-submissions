class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        # use dfs to calculate
        def dfs(r, c):
            # nonlocal maxArea
            if (r not in range(rows) or # stopping condition (NOT A 1)
            c not in range(cols) or
            (r,c) in visited or
            grid[r][c] == 0):
                return 0

            visited.add((r, c))
            return (1 + dfs(r + 1, c) + # run dfs in every direction but adding 1 since the tile we're on counts as a 1
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c -1))

        area = 0
        for r in range(rows):
            for c in range(cols): # when we hit a 1 we want to call dfs and explore it fully
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c)) # will return the maxValue seen so far?

        return area