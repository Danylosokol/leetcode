class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        L, R = 0, 0

        while R < len(nums):
            if currSum < 0:
                L = R 
                currSum = nums[R]
            else:
                currSum += nums[R]
            maxSum = max(currSum, maxSum)
            R += 1
        
        return maxSum