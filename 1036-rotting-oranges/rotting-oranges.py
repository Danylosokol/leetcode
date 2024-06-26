class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        fresh = 0
        time = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if (
                        new_row not in range(rows) or
                        new_col not in range(cols) or
                        grid[new_row][new_col] != 1 or
                        (new_row, new_col) in visited
                    ):
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
            
