class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return false
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        row = 0

        while top <= bottom:
            mid = (top + bottom)//2

            if target > matrix[mid][right]:
                top = mid + 1
            elif target < matrix[mid][left]:
                bottom = mid - 1
            else:
                row = mid
                break

        if top > bottom:
            return False

        while left <= right:
            mid = (left + right)//2

            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        
        return False