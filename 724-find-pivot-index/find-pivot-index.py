class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        curr = 0

        for num in nums:
            curr += num
            prefix.append(curr)
        
        for i in range(len(nums)):
            leftSum = prefix[i - 1] if i > 0 else 0
            rightSum = prefix[-1] - prefix[i]
            if leftSum == rightSum:
                return i

        return -1