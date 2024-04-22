class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
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
                if r == rows - 1:
                    prev_row[-1] = 0

            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0
                    continue
                curr_row[c] = prev_row[c] + curr_row[c + 1]
            print("new_row:")
            print(r)
            print(curr_row)
            prev_row = curr_row

        return prev_row[0]
