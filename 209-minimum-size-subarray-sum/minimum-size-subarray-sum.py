class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        currLen = 0
        L = 0

        for R in range(len(nums)):
            currLen += nums[R]
            while currLen >= target:
                minLen = min(minLen, R - L + 1)
                currLen -= nums[L]
                L += 1
            
        return minLen if minLen != float('inf') else 0