class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        prevPrefix = [0] * len(matrix[0])
        for i in range(len(matrix)):
            curr = 0
            currPrefix = []
            for j in range(len(matrix[i])):
                curr += matrix[i][j]
                currPrefix.append(curr + prevPrefix[j])
            self.prefix.append(currPrefix)
            prevPrefix = currPrefix
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumCol1 = 0
        if row1 > 0:
            if col1 > 0:
                sumCol1 = self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col1 - 1]
            sumCol2 = self.prefix[row2][col2] - self.prefix[row1 - 1][col2]
        else:
            if col1 > 0:
                sumCol1 = self.prefix[row2][col1 - 1]
            sumCol2 = self.prefix[row2][col2]          
        return sumCol2 - sumCol1


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)