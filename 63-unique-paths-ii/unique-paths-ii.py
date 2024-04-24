class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[-1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c < cols - 1:
                    dp[c] = dp[c] + dp[c + 1]
        
        return dp[0]