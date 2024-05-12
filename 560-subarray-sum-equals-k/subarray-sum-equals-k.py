class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqSum = {0: 1}
        result = 0
        curr = 0
        for num in nums:
            curr += num
            diff = curr - k
            result += freqSum.get(diff, 0)
            freqSum[curr] = 1 + freqSum.get(curr, 0)
        return result