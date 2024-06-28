class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum/2)

        N, M = len(stones), target
        dp = [0] * (M + 1)

        for c in range(M + 1):
            if c >= stones[0]:
                dp[c] = stones[0]
        
        for i in range(1, N):
            newRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0
                if c - stones[i] >= 0:
                    include = stones[i] + dp[c - stones[i]]
                newRow[c] = max(skip, include)
            dp = newRow
        
        return abs(dp[M] - (stoneSum - dp[M]))