class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                next_dp.add(t + nums[i])
            dp |= next_dp # join two sets, we could also add t to next_dp and just copy next_dp completely to dp.
        
        return target in dp 