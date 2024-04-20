class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums))]

        def rob_rec(nums, idx):
            if idx < 0:
                return 0
            
            if memo[idx] >= 0:
                return memo[idx]
            
            result = max(rob_rec(nums, idx -2) + nums[idx], rob_rec(nums, idx-1))
            memo[idx] = result
            return result
        
        return rob_rec(nums, len(nums) -1)