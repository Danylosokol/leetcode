class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        df = {}

        def backtrack(index, sum):
            if index >= len(nums):
                return 1 if sum == target else 0
            
            if (index, sum) in df:
                return df[(index, sum)]
            
            df[(index, sum)] = backtrack(index + 1, sum + nums[index]) + backtrack(index + 1, sum - nums[index])
            return df[(index, sum)]
        
        return backtrack(0, 0)