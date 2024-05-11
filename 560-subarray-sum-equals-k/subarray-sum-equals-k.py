class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqSum = {0: 1}
        result = 0
        currSum = 0

        for num in nums:
            currSum += num
            diff = currSum - k
            result += freqSum.get(diff, 0)
            freqSum[currSum] = 1 + freqSum.get(currSum, 0)
        
        return result