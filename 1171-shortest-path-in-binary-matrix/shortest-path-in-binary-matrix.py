class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while queue:
            row, col, length = queue.popleft()

            if min(row, col) < 0 or max(row, col) >= n or grid[row][col] == 1:
                continue
            
            if row == n-1 and col == n-1:
                return length
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, length + 1))
                    visited.add((new_row, new_col))
        
        return -1 