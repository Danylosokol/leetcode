class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float('inf')
        currSum = 0
        L = 0
        for R in range(len(nums)):
            currSum += nums[R]

            while currSum >= target:
                minSize = min(minSize, R - L + 1)
                currSum -= nums[L]
                L += 1
        
        return minSize if minSize != float('inf') else 0