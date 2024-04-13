class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1]:
            return -1

        def bfs(r, c):
            queue = deque()
            visited = set()
            queue.append((r, c))
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
            length = 1

            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    if row == rows - 1 and col == cols - 1:
                        return length
                        
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
                length += 1
            
            return -1
        
        return bfs(0, 0)