class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0

        prev1 = 0
        prev2 = 0

        for n in nums:
            temp = max(prev1 + n, prev2)
            prev1 = prev2
            prev2 = temp
        
        return prev2