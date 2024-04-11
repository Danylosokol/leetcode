class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        max_size = 0

        def dfs(r, c):
            if (r) not in range(rows) or (c) not in range(cols) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            size = 1
            size += dfs(r + 1, c)
            size += dfs(r, c + 1)
            size += dfs(r - 1, c)
            size += dfs(r, c - 1)
            return size


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size = dfs(r, c)
                    max_size = max(size, max_size)
        
        return max_size
