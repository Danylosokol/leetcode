class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            size = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        size += 1
            
            return size

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    size = bfs(r, c)
                    max_size = max(max_size, size)
        
        return max_size