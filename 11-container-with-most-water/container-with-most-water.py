class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        L, R = 0, len(height) - 1

        while L < R:
            area = min(height[L], height[R]) * (R - L)
            result = max(result, area)

            if height[L] <= height[R]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
        
        return result