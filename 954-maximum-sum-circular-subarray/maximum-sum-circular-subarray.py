class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)

            total += num

            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)
        
        return max(globMax, total - globMin) if globMax > 0 else globMax