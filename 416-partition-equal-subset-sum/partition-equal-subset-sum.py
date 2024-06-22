class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        capacity = sum(nums) / 2
        if not capacity.is_integer():
            return False
        N, M = len(nums), int(capacity)
        dp = [0] * (M + 1)

        for c in range(M + 1):
            if nums[0] <= c:
                dp[c] = nums[0]
 
        for i in range(1, N):
            cur_row = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0 
                if c - nums[i] >= 0:
                    include = nums[i] + dp[c - nums[i]]
                cur_row[c] = max(skip, include)
            dp = cur_row

        return dp[M] == capacity