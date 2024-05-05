class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxAmount = 0
        while L < R:
            maxAmount = max(maxAmount, (min(height[L], height[R]) * (R - L)))
            if height[L] <= height[R]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
        return maxAmount
