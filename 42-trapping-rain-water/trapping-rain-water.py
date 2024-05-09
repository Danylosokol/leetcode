class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        result = 0
        maxLevel = 0 

        while L < R:
            if height[L] <= height[R]:
                maxLevel = max(height[L], maxLevel)
                result += maxLevel - height[L]
                L += 1
            elif height[R] < height[L]:
                maxLevel = max(height[R], maxLevel)
                result += maxLevel - height[R]
                R -= 1
        
        return result