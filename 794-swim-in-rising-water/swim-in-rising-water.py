class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        min_heap = [[grid[0][0], 0, 0]]

        visited = set()
        visited.add(grid[0][0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if(
                    max(nr, nc) < N and min(nr,  nc) >= 0 and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))
