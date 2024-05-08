class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        reversedPrefix = []  
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        
        curr = 0
        for num in reversed(nums):
            curr += num
            reversedPrefix.insert(0, curr)

        for i in range(len(nums)):
            if prefix[i] == reversedPrefix[i]:
                return i
        
        return -1