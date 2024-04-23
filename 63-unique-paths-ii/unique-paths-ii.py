class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        prev_row = [0] * cols
        prev_row[-1] = 1

        for r in range(rows - 1, -1, -1):
            curr_row = [0] * cols
            if obstacleGrid[r][-1] == 1 or prev_row[-1] == 0:
                curr_row[-1] = 0
            else:
                curr_row[-1] = 1
            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0
                else:
                    curr_row[c] = prev_row[c] + curr_row[c+1]
            print("current row:")
            print(curr_row)
            prev_row = curr_row
        
        return prev_row[0]