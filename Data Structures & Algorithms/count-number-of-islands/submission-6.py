class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]] # 4 directions
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                            q.append((r, c))
                            visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited: # valid cell, want to keep exploring
                    bfs(r, c)
                    islands += 1
        return islands
