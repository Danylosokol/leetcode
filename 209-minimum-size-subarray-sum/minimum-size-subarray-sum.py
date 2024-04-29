class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        default_len = len(nums) + 1
        length = default_len
        total = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if length == default_len else length