class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        df = set()
        df.add(0)

        for i in range(len(nums) - 1, -1, -1):
            next_df = set()
            for t in df:
                next_df.add(t + nums[i])
            df |= next_df
        
        return target in df