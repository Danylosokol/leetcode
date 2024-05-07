class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.matrixPrefix = []
        for i in range(len(matrix)):
            curr = 0
            prefix = []
            for num in matrix[i]:
                curr += num
                prefix.append(curr)
            self.matrixPrefix.append(prefix)
        print(self.matrixPrefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            rightSum = self.matrixPrefix[i][col2]
            leftSum = self.matrixPrefix[i][col1 - 1] if col1 > 0 else 0
            # print("sum for row:")
            # print(i)
            sum += rightSum - leftSum
            # print(sum)
        return sum 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)