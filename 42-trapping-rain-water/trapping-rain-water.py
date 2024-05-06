class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        result = 0

        while L < R:
            if height[L] <= height[R]:
                L += 1
                maxL = max(maxL, height[L])
                result += maxL - height[L]
            elif height[R] < height[L]:
                R -= 1
                maxR = max(maxR, height[R])
                result += maxR - height[R]
        
        return result