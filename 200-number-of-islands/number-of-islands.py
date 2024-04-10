class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        visited = set()
        numOfRow = len(grid)
        numOfColls = len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == numOfRow or c == numOfColls or (r, c) in visited or grid[r][c] == "0":
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1
        return counter