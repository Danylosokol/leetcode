class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0

        memo = [0 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            val = nums[i]
            memo[i + 1] = max(memo[i], memo[i - 1] + val)
        
        return memo[-1]