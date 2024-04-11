class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr) in range(rows) and (nc) in range(cols) and (nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
        
