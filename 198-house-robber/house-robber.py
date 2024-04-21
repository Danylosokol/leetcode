class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        # house before previous
        prev1 = 0
        # previsous house
        prev2 = 0

        for num in nums:
            # compute max that we can rob up until current house
            temp = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = temp

        return prev2