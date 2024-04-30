class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        currSum = 0
        R = L = 0

        while R < len(nums):
            currSum += nums[R]
            while currSum >= target:
                minLength = min(minLength, R - L + 1)
                currSum -= nums[L]
                L += 1
            R += 1
        
        return minLength if minLength != len(nums) + 1 else 0

