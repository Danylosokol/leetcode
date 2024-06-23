class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        capacity = sum(nums) // 2
        N, M = len(nums), capacity
        df = [0] * (M + 1)

        for c in range(M + 1):
            if nums[0] <= c:
                df[c] = nums[0]

        for i in range(1, N):
            new_row = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = df[c]
                include = 0
                if c - nums[i] >= 0:
                    include = nums[i] + df[c - nums[i]]
                new_row[c] = max(skip, include)
            df = new_row

        return df[M] == capacity
        